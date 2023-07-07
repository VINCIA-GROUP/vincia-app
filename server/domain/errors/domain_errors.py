from domain.errors.api_exception import ApiError

class ChatError(ApiError):
    def __init__(self):
        super().__init__("2001", "Chat Error")

class HistoryOfQuestionNotFound(ApiError):
    def __init__(self):
        super().__init__("2002", "History of question not found.")
        
class ChatNotFound(ApiError):
    def __init__(self):
        super().__init__("2003", "Chat not found.")