from abc import ABC, abstractmethod
from .dto import UserAccountDTO, AuthCommand, ChangeUserInfoCommand, ChangePasswordCommand

class AbstractAuthService(ABC):
    @abstractmethod
    def authenticate(self, auth_command: AuthCommand) -> UserAccountDTO: ...
    
    @abstractmethod
    def refresh_token(self, refresh_token: str) -> str: ...
    
    @abstractmethod
    def logout(self, access_token: str) -> None: ...


class AbstractUserAccountService(ABC):
    @abstractmethod
    def register(self, auth_command: AuthCommand) -> UserAccountDTO: ...
    
    @abstractmethod
    def change_user_info(self, command: ChangeUserInfoCommand) -> UserAccountDTO: ...
    
    @abstractmethod
    def change_password(self, command: ChangePasswordCommand) -> None: ...