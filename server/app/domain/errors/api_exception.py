class ApiError():
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def to_json(self):
        return {"code":self.code, "message":self.message}   

class ApiException(Exception):
    def __init__(self, error=None):
        self.errors = []
        if(error != None):
            self.errors.append(error)
      
    def append(self, error: ApiError):
          self.errors.append(error)
    
    def to_json(self):
        return list(map(lambda x: x.to_json(), self.errors))
