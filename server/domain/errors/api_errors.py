        
class ApiError(Exception):
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message



class DeuMerda(ApiError):
    def __init__(self):
        super().__init__("78", "Deu merda exception")
