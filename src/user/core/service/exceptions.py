from src.user.core.domain.exceptions import UserAccountException

class UserServiceException(UserAccountException):
    def __init__(self, message: str, code: int, *args: object) -> None:
        super().__init__(message, code, *args)
    
    @classmethod
    def no_strategy_found(cls, type: str) -> "UserServiceException":
        return cls(f"No hay una estrategia definida para: {type}", 8)
    
    @classmethod
    def user_not_found(cls, identifier: str) -> "UserServiceException":
        return cls(f"Usuario no encontrado: {identifier}", 9)
    
    @classmethod
    def invalid_password_verification_code(cls) -> "UserServiceException":
        return cls("Código de verificación inválido", 10)