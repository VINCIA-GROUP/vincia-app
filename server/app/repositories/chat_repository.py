from psycopg2 import DatabaseError
from app.domain.entities.chat_messages import ChatMessages

class ChatRepository():
    def __init__(self, connection): 
        self.connection = connection   
        
    def insert_range_messages(self, chat_messages, user_id):
        try:
            cursor = self.connection.cursor()
            for message in chat_messages:
                cursor.execute("INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date, sequence) VALUES (%s, %s, %s, %s, %s, %s, %s);", (message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date, message.sequence))
            cursor.close()
            return True
        except DatabaseError as error:
            print('ChatRepository - insert_range_messages - ' + error)
            return False
        
    def insert_message(self, message, user_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date, sequence) VALUES (%s, %s, %s, %s, %s, %s, %s);", (message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date, message.sequence))
            cursor.close()
            return True
        except DatabaseError as error:
            print('ChatRepository - insert_message - ' + error)
            return False


    def get_by_history_question_id(self, history_question_id, user_id):
        messages = [] 
        try:
            cursor = self.connection.cursor()  
            cursor.execute("SELECT * FROM chats_messages c WHERE c.history_of_question_id = %s and c.user_id = %s;", (history_question_id, user_id,))
            rows = cursor.fetchall()
            for row in rows:
                message = ChatMessages(*row)
                messages.append(message)            
            messages = sorted(messages, key = lambda obj: obj.sequence)
            cursor.close()
        except DatabaseError as error:
            print('ChatRepository - get_by_history_question_id - ' + error)
        return messages
    
    def commit(self):
        try:
            self.connection.commit()
            return True
        except DatabaseError as error:
            print('QuestionsRepository - commit - ' + error)
            return False
      
    def rollback(self):
        try:
            self.connection.rollback()
            return True
        except DatabaseError as error:
            print('QuestionsRepository - rollback - ' + error)
            return False