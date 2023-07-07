from domain.entities.chat_messages import ChatMessages
from domain.errors.api_exception import ApiException
from domain.errors.domain_errors import ChatNotFound
from infra.repositories.repository import Repository


class ChatRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def insert_range_messages(self, chat_messages, user_id):
        cursor = self.conn.cursor()
        for message in chat_messages:
            cursor.execute("INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date) VALUES (%s, %s, %s, %s, %s, %s);", (message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date))
        cursor.close()
        
    def insert_message(self, message, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date) VALUES (%s, %s, %s, %s, %s, %s);", (message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date))
        cursor.close()


    def get_by_history_question_id(self, history_question_id, user_id):
        cursor = self.conn.cursor()  
        cursor.execute("SELECT c.id, c.history_of_question_id, c.role, c.content, c.create_date FROM chats_messages c WHERE c.history_of_question_id = %s and c.user_id = %s;", (history_question_id, user_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            raise ApiException(ChatNotFound())
        messages_tuple = cursor.fetchall()
        messages = [] 
        for message_tuple in messages_tuple:
            message_id, message_history_of_question_id, message_role, message_content, message_create_date = message_tuple
            messages.append(ChatMessages(message_id, message_history_of_question_id, message_role, message_content, message_create_date))
        messages_sorted = sorted(messages, key = lambda obj: obj.create_date)
        cursor.close()
        return messages_sorted
    
