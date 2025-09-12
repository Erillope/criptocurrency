from abc import ABC, abstractmethod
from src.user.core.service.abstract_auth_service import AbstractAuthService, AbstractUserAccountService
from src.user.core.service.abstract_auth_strategies import AuthStrategy
from src.user.core.service.abstract_register_strategies import RegisterStrategy
from src.user.core.service.dto import PasswordAuthCommand, TokenAuthCommand, AuthTokenType
from src.user.core.service.token_manager import TokenManager
from src.user.core.service.repository import GetUserRepository
from src.user.core.service.password_code_verifier import PasswordCodeVerifier
from typing import Mapping

class UserSistemConfigBuilder(ABC):
    @abstractmethod
    def get_auth_service(self) -> AbstractAuthService: ...

    @abstractmethod
    def get_user_account_service(self) -> AbstractUserAccountService: ...

    @abstractmethod
    def get_password_auth_strategy(self) -> AuthStrategy[PasswordAuthCommand]: ...

    @abstractmethod
    def get_token_auth_strategies(self) -> Mapping[AuthTokenType, AuthStrategy[TokenAuthCommand]]: ...

    @abstractmethod
    def get_token_manager(self) -> TokenManager: ...

    @abstractmethod
    def get_password_register_strategy(self) -> RegisterStrategy[PasswordAuthCommand]: ...

    @abstractmethod
    def get_token_register_strategies(self) -> Mapping[AuthTokenType, RegisterStrategy[TokenAuthCommand]]: ...

    @abstractmethod
    def get_get_user_repository(self) -> GetUserRepository: ...

    @abstractmethod
    def get_password_code_verifier(self) -> PasswordCodeVerifier: ...