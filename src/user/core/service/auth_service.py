from .abstract_auth_service import AbstractAuthService, AbstractUserAccountService
from .dto import (UserAccountDTO, AuthCommand, ChangeUserInfoCommand, AuthTokenType,
                  ChangePasswordCommand, PasswordAuthCommand, TokenAuthCommand, UserIdentifier)
from .abstract_auth_strategies import AuthStrategy
from .abstract_register_strategies import RegisterStrategy
from .password_code_verifier import PasswordCodeVerifier
from .token_manager import TokenManager
from .repository import GetUserRepository
from pydantic import BaseModel
from typing import Mapping
from .exceptions import UserServiceException
from src.user.core.domain.values import UserUpdateData
from src.user.core.domain.user_account import UserAccount

class AuthService(BaseModel, AbstractAuthService):
    password_auth: AuthStrategy[PasswordAuthCommand]
    token_auth_strategies: Mapping[AuthTokenType, AuthStrategy[TokenAuthCommand]]
    token_manager: TokenManager

    def authenticate(self, auth_command: AuthCommand) -> UserAccountDTO:
        if isinstance(auth_command, PasswordAuthCommand):
            return self.password_auth.authenticate(auth_command)
        elif isinstance(auth_command, TokenAuthCommand):
            return self._auth_by_token(auth_command)
        else:
            raise UserServiceException.no_strategy_found(auth_command.__class__.__name__)

    def refresh_token(self, refresh_token: str) -> str:
        return self.token_manager.refresh(refresh_token)

    def logout(self, access_token: str) -> None:
        self.token_manager.invalidate(access_token)

    def _auth_by_token(self, auth_command: TokenAuthCommand) -> UserAccountDTO:
        strategy = self.token_auth_strategies.get(auth_command.token_type)
        if not strategy:
            raise UserServiceException.no_strategy_found(str(auth_command.token_type))
        return strategy.authenticate(auth_command)
    
    model_config = {
        "arbitrary_types_allowed": True
    }


class UserAccountService(BaseModel, AbstractUserAccountService):
    password_register: RegisterStrategy[PasswordAuthCommand]
    token_register_strategies: Mapping[AuthTokenType, RegisterStrategy[TokenAuthCommand]]
    get_user_repository: GetUserRepository
    password_code_verifier: PasswordCodeVerifier

    def register(self, auth_command: AuthCommand) -> UserAccountDTO:
        if isinstance(auth_command, PasswordAuthCommand):
            return self.password_register.register(auth_command)
        elif isinstance(auth_command, TokenAuthCommand):
            return self._register_by_token(auth_command)
        else:
            raise UserServiceException.no_strategy_found(auth_command.__class__.__name__)

    def change_user_info(self, command: ChangeUserInfoCommand) -> UserAccountDTO:
        user = self._search_user(command.id)
        user.update(command.to_update_data())
        return UserAccountDTO.from_user_model(user)

    def change_password(self, command: ChangePasswordCommand) -> None:
        user = self._search_user(command.id)
        if not self.password_code_verifier.verify(command.verification_code, user.id):
            raise UserServiceException.invalid_password_verification_code()
        user.update(UserUpdateData(password=command.new_password))

    def send_password_reset_code(self, user_identifier: UserIdentifier) -> None:
        user = self._search_user(user_identifier)
        self.password_code_verifier.send_code(user.id)
    
    def get_user_data(self, identifier: UserIdentifier) -> UserAccountDTO:
        user = self._search_user(identifier)
        return UserAccountDTO.from_user_model(user)
    
    def _register_by_token(self, auth_command: TokenAuthCommand) -> UserAccountDTO:
        strategy = self.token_register_strategies.get(auth_command.token_type)
        if not strategy:
            raise UserServiceException.no_strategy_found(str(auth_command.token_type))
        return strategy.register(auth_command)
    
    def _search_user(self, identifier: UserIdentifier) -> UserAccount:
        if not self.get_user_repository.exists(identifier):
            raise UserServiceException.user_not_found(identifier.id)
        return self.get_user_repository.get(identifier)
    
    model_config = {
        "arbitrary_types_allowed": True
    }