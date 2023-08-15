from app.domain.entities.chat_messages import ChatMessages
from app.repositories.repository import Repository

class ChatRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, ChatMessages)  
        
    def insert_range_messages(self, chat_messages, user_id):
        for message in chat_messages:
            result = super().update(
                query="INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date, sequence) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                params=(message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date, message.sequence)
            )
        
    def insert_message(self, message, user_id):
        super().update(
            query="INSERT INTO chats_messages (id, history_of_question_id, user_id, role, content, create_date, sequence) VALUES (%s, %s, %s, %s, %s, %s, %s);",
            params=(message.id, message.history_of_question_id, user_id, message.role, message.content, message.create_date, message.sequence)
        )

    def get_by_history_question_id(self, history_question_id, user_id):
        messages = super().get_many(
            query="SELECT c.id, c.history_of_question_id, c.role, c.content, c.create_date, c.sequence FROM chats_messages c WHERE c.history_of_question_id = %s and c.user_id = %s;", 
            params=(history_question_id, user_id,)
        )
        messages = sorted(messages, key = lambda obj: obj.sequence)
        return messages