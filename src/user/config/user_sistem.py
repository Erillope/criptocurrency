from .user_sistem_config import UserSistemConfigBuilder
from pydantic import BaseModel, PrivateAttr
from src.user.core.service.abstract_auth_service import AbstractAuthService, AbstractUserAccountService
from src.user.core.service.abstract_auth_strategies import AuthStrategy
from src.user.core.service.abstract_register_strategies import RegisterStrategy
from src.user.core.service.dto import PasswordAuthCommand, TokenAuthCommand, AuthTokenType
from src.user.core.service.token_manager import TokenManager
from src.user.core.service.repository import GetUserRepository
from src.user.core.service.password_code_verifier import PasswordCodeVerifier
from src.user.core.service.auth_service import AuthService, UserAccountService
from typing import Mapping, Optional

class DefaultUserSistemConfigBuilder(BaseModel, UserSistemConfigBuilder):
    _auth_service: Optional[AbstractAuthService] = PrivateAttr(None)
    _user_account_service: Optional[AbstractUserAccountService] = PrivateAttr(None)
    _password_auth_strategy: Optional[AuthStrategy[PasswordAuthCommand]] = PrivateAttr(None)
    _token_auth_strategies: Mapping[AuthTokenType, AuthStrategy[TokenAuthCommand]] = PrivateAttr({})
    _token_manager: Optional[TokenManager] = PrivateAttr(None)
    _password_register_strategy: Optional[RegisterStrategy[PasswordAuthCommand]] = PrivateAttr(None)
    _token_register_strategies: Mapping[AuthTokenType, RegisterStrategy[TokenAuthCommand]] = PrivateAttr({})
    _get_user_repository: Optional[GetUserRepository] = PrivateAttr(None)
    _password_code_verifier: Optional[PasswordCodeVerifier] = PrivateAttr(None)

    def get_auth_service(self) -> AbstractAuthService:
        if self._auth_service is None:
            self._auth_service = AuthService(
                password_auth = self.get_password_auth_strategy(),
                token_auth_strategies = self.get_token_auth_strategies(),
                token_manager = self.get_token_manager()
            )
        return self._auth_service

    def get_user_account_service(self) -> AbstractUserAccountService:
        if self._user_account_service is None:
            self._user_account_service = UserAccountService(
                password_register = self.get_password_register_strategy(),
                token_register_strategies = self.get_token_register_strategies(),
                get_user_repository = self.get_get_user_repository(),
                password_code_verifier = self.get_password_code_verifier()
            )
        return self._user_account_service
    
    def get_password_auth_strategy(self) -> AuthStrategy[PasswordAuthCommand]:
        if self._password_auth_strategy is None:
            raise NotImplementedError("Password auth strategy is not set")
        return self._password_auth_strategy
    
    def get_token_auth_strategies(self) -> Mapping[AuthTokenType, AuthStrategy[TokenAuthCommand]]:
        return self._token_auth_strategies
    
    def get_token_manager(self) -> TokenManager:
        if self._token_manager is None:
            raise NotImplementedError("Token manager is not set")
        return self._token_manager
    
    def get_password_register_strategy(self) -> RegisterStrategy[PasswordAuthCommand]:
        if self._password_register_strategy is None:
            raise NotImplementedError("Password register strategy is not set")
        return self._password_register_strategy
    
    def get_token_register_strategies(self) -> Mapping[AuthTokenType, RegisterStrategy[TokenAuthCommand]]:
        return self._token_register_strategies
    
    def get_get_user_repository(self) -> GetUserRepository:
        if self._get_user_repository is None:
            raise NotImplementedError("Get user repository is not set")
        return self._get_user_repository
    
    def get_password_code_verifier(self) -> PasswordCodeVerifier:
        if self._password_code_verifier is None:
            raise NotImplementedError("Password code verifier is not set")
        return self._password_code_verifier