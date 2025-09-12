from src.user.core.service.abstract_auth_strategies import AuthStrategy
from src.user.core.service.dto import PasswordAuthCommand, UserAccountDTO, TokenAuthCommand, UserIdentifier
from src.user.core.service.token_manager import TokenManager
from src.user.core.service.abstract_register_strategies import RegisterStrategy
from src.user.core.service.repository import GetUserRepository
from src.user.core.service.password_code_verifier import PasswordCodeVerifier
from src.user.core.domain.user_account import UserAccount
from typing import Optional

def dummy_user_account_dto(username: str = "dummy_user") -> UserAccountDTO:
    return UserAccountDTO(
        id="dummy_id",
        name="Dummy User",
        email="dummy_email@example.com",
        username=username,
    )

class StubPasswordAuthStrategy(AuthStrategy[PasswordAuthCommand]):
    def __init__(self, authenticate_value: Optional[UserAccountDTO] = None):
        super().__init__()
        self.authenticate_value = authenticate_value

    def authenticate(self, command: PasswordAuthCommand) -> UserAccountDTO:
        return self.authenticate_value or dummy_user_account_dto(username=command.username)

class StubTokenAuthStrategy(AuthStrategy[TokenAuthCommand]):
    def __init__(self, authenticate_value: Optional[UserAccountDTO] = None):
        super().__init__()
        self.authenticate_value = authenticate_value

    def authenticate(self, command: TokenAuthCommand) -> UserAccountDTO:
        return self.authenticate_value or dummy_user_account_dto(username=command.token)

class StubTokenManager(TokenManager):
    def __init__(self, refresh_value: Optional[str] = None):
        super().__init__()
        self.refresh_value = refresh_value or "dummy_new_access_token"

    def refresh(self, refresh_token: str) -> str:
        return self.refresh_value

    def invalidate(self, access_token: str) -> None:
        return None

class StubPasswordRegisterStrategy(RegisterStrategy[PasswordAuthCommand]):
    def __init__(self, register_value: Optional[UserAccountDTO] = None):
        super().__init__()
        self.register_value = register_value

    def register(self, command: PasswordAuthCommand) -> UserAccountDTO:
        return self.register_value or dummy_user_account_dto(username=command.username)

class StubTokenRegisterStrategy(RegisterStrategy[TokenAuthCommand]):
    def __init__(self, register_value: Optional[UserAccountDTO] = None):
        super().__init__()
        self.register_value = register_value

    def register(self, command: TokenAuthCommand) -> UserAccountDTO:
        return self.register_value or dummy_user_account_dto(username=command.token)

class StubGetUserRepository(GetUserRepository):
    def __init__(self, get_value: Optional[UserAccount] = None, exists_value: bool = True):
        super().__init__()
        self.get_value = get_value
        self.exists_value = exists_value

    def get(self, identifier: UserIdentifier) -> UserAccount:
        return self.get_value or UserAccount(
            id=identifier.id,
            name="Dummy User",
            email="dummy_email@example.com",
            username="dummy_user"
        )
    
    def exists(self, identifier: UserIdentifier) -> bool:
        return self.exists_value

class StubPasswordCodeVerifier(PasswordCodeVerifier):
    def __init__(self, verify_value: bool = True):
        super().__init__()
        self.verify_value = verify_value

    def verify(self, code: str, user_id: str) -> bool:
        return self.verify_value
    
    def send_code(self, user_id: str) -> None:
        return None