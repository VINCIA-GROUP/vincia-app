import openai
import uuid
import datetime
from bs4 import BeautifulSoup
from domain.entities.chat_messages import ChatMessages
from domain.errors.api_exception import ApiException
from domain.errors.domain_errors import ChatError, ChatNotFound, HistoryOfQuestionNotFound

class ChatService:
    def __init__(self, history_question_repository, question_repository, chat_repository):
        self.history_question_repository = history_question_repository
        self.question_repository = question_repository
        self.chat_repository = chat_repository
        
    def send_message(self, user_id, history_question_id, message):
        
        # Verificar se já existe um chat: serach(user_id, history_id)
        chat_messages = None
        try:
            chat_messages = self.chat_repository.get_by_history_question_id(history_question_id, user_id)
        except ApiException as error:
            if(any(isinstance(item, ChatNotFound) for item in error.errors)):
                chat_messages = self.create_new_chat(history_question_id, user_id)
            else:
                raise error
        
        user_message = ChatMessages(str(uuid.uuid4()), history_question_id, "user", message, datetime.datetime.now() + datetime.timedelta(milliseconds=2))
        chat_messages.append(user_message)
        messages = list(map(lambda x : x.to_json(), chat_messages))
        
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages,
            temperature = 0.3
            )
            assistant_message = ChatMessages(str(uuid.uuid4()), history_question_id, "assistant", response.choices[0].message.content, datetime.datetime.now() + datetime.timedelta(milliseconds=3))
            self.chat_repository.insert_range_messages([user_message, assistant_message], user_id)
            self.chat_repository.unit_of_work()
            return response.choices[0].message.content
        except Exception as e:
            raise ApiException(ChatError())

       
        
    def create_new_chat(self,  history_question_id, user_id):
        history_question = self.history_question_repository.get_by_id(history_question_id, user_id)
        question = self.question_repository.get_by_id(history_question.question_id)
        messages = self.generate_initial_messages(question, history_question_id)
        self.chat_repository.insert_range_messages(messages, user_id)
        return messages

        
    def generate_initial_messages(self, question, history_question_id):
        alternatives = ""
        letter = "A"
        answer = ""
        messages = []
        statement = self.remover_tags_img(question.statement)
        for index, value in enumerate(question.alternatives):
            alternatives += f"{chr(ord(letter) + index)}){value.text}"
            if(value.id == question.answer):
                answer = f"{chr(ord(letter) + index)}){value.text}"
        chat_message_system = ChatMessages(str(uuid.uuid4()), history_question_id,  "system",  
                                    f"Você é o Vincia Bot, um professor que irá tirar todas as dúvidas que o aluno tiver em relação a seguinte questão '{statement}' com as alternativas '{alternatives}', sendo a resposta certa a alternativa '{answer}'", datetime.datetime.now())
        
        chat_message_assistant = ChatMessages(str(uuid.uuid4()),  history_question_id,  "assistant", "Olá, sou o Vincia Bot é irei esclarecer todas as suas dúvidas. Como posso te ajudar?",  datetime.datetime.now()+ datetime.timedelta(milliseconds=1))
        return [chat_message_system, chat_message_assistant]
    
    def remover_tags_img(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img'):
            img.decompose()  # Remove a tag <img> e seu conteúdo
        return str(soup)
    
