from app.domain.errors.api_exception import ApiError

class AuthorizationHeaderMissing(ApiError):
    def __init__(self):
        super().__init__("1001", "Authorization header is expected")

class InvalidHeaderToken(ApiError):
    def __init__(self):
        super().__init__("1002", "Authorization header must start with Bearer")

class TokenNotFound(ApiError):
    def __init__(self):
        super().__init__("1003", "Token not found")

class TokenExpired(ApiError):
    def __init__(self):
        super().__init__("1004", "Token is expired")

class InvalidClaims(ApiError):
    def __init__(self):
        super().__init__("1005", "Incorrect claims, please check the audience and issuer")

class PermissionDenid(ApiError):
    def __init__(self):
        super().__init__("1006", "Not permission token")
        
class InalidToken(ApiError):
    def __init__(self):
        super().__init__("1007", "Unable to parse authentication")

class UnableFindKey(ApiError):
    def __init__(self):
        super().__init__("1008", "Unable to find appropriate key")
    

