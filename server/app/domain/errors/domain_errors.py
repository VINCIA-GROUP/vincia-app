from app.domain.errors.api_exception import ApiError

class ChatError(ApiError):
    def __init__(self):
        super().__init__("2001", "Chat Error")

class HistoryOfQuestionNotFound(ApiError):
    def __init__(self):
        super().__init__("2002", "History of question not found.")
        
class ChatNotFound(ApiError):
    def __init__(self):
        super().__init__("2003", "Chat not found.")
        

class HistoryOfQuestionIdInvalid(ApiError):
    def __init__(self):
        super().__init__("2004", "The history of question id is invalid.")
        
class AbilityNotFound(ApiError):
    def __init__(self):
        super().__init__("2005", "no ability found.")
        
class QuestionNotFound(ApiError):
    def __init__(self):
        super().__init__("2006", "no question found.")
        
class AbilityRatingCreateFailed(ApiError):
    def __init__(self):
        super().__init__("2007", "ability rating creation failed.")
        
class DataNotFound(ApiError):
    def __init__(self, table,  params):
        super().__init__("2008", f"No data with parameters {table}, found in table {params}.")