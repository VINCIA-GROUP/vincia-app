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

        chat_messages = self.chat_repository.get_by_history_question_id(history_question_id, user_id)
        if(chat_messages == None):
            chat_messages = self.create_new_chat(history_question_id, user_id)

        user_message = ChatMessages(str(uuid.uuid4()), history_question_id, "user", message, datetime.datetime.now(), chat_messages[-1].sequence + 1)
        chat_messages.append(user_message)
        messages = list(map(lambda x : x.to_json(), chat_messages))
        
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages = messages,
            temperature = 0.3
            )
            assistant_message = ChatMessages(str(uuid.uuid4()), history_question_id, "assistant", response.choices[0].message.content, datetime.datetime.now(), chat_messages[-1].sequence + 1)
            self.chat_repository.insert_range_messages([user_message, assistant_message], user_id)
            self.chat_repository.commit()
            return response.choices[0].message.content
        except Exception as e:
            raise ApiException(ChatError())

       
        
    def create_new_chat(self,  history_question_id, user_id):
        question_id = self.history_question_repository.get_question_id(history_question_id, user_id)
        if(question_id == None):
            raise ApiException(HistoryOfQuestionNotFound())
        question = self.question_repository.get_by_id(question_id)
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
                                    f"Você é o Vincia Bot, um professor que irá tirar todas as dúvidas que o aluno tiver em relação a seguinte questão '{statement}' com as alternativas '{alternatives}', sendo a resposta certa a alternativa '{answer}'", datetime.datetime.now(), 1)
        
        chat_message_assistant = ChatMessages(str(uuid.uuid4()),  history_question_id,  "assistant", "Olá, sou o Vincia Bot é irei esclarecer todas as suas dúvidas. Como posso te ajudar?",  datetime.datetime.now(), 2)
        return [chat_message_system, chat_message_assistant]
    
    def remover_tags_img(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img'):
            img.decompose()  # Remove a tag <img> e seu conteúdo
        return str(soup)
    
