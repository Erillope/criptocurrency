from .abstract_auth_service import AbstractAuthService, AbstractUserAccountService
from .dto import UserAccountDTO, AuthCommand, ChangeUserInfoCommand, ChangePasswordCommand

class AuthService(AbstractAuthService):
    def authenticate(self, auth_command: AuthCommand) -> UserAccountDTO:
        raise NotImplementedError("Method authenticate not implemented")

    def refresh_token(self, refresh_token: str) -> str:
        raise NotImplementedError("Method refresh_token not implemented")

    def logout(self, access_token: str) -> None:
        raise NotImplementedError("Method logout not implemented")


class UserAccountService(AbstractUserAccountService):
    def register(self, auth_command: AuthCommand) -> UserAccountDTO:
        raise NotImplementedError("Method register not implemented")

    def change_user_info(self, command: ChangeUserInfoCommand) -> UserAccountDTO:
        raise NotImplementedError("Method change_user_info not implemented")

    def change_password(self, command: ChangePasswordCommand) -> None:
        raise NotImplementedError("Method change_password not implemented")