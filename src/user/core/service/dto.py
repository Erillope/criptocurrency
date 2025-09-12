from pydantic import BaseModel
from typing import Optional
from enum import Enum
from abc import ABC
from src.user.core.domain.user_account import UserAccount
from src.user.core.domain.values import UserUpdateData

class AuthTokenType(str, Enum):
    GOOGLE = "google"
    FACEBOOK = "facebook"

class IdentifierType(str, Enum):
    EMAIL = "email"
    USERNAME = "username"
    ID = "id"

class AuthCommand(BaseModel, ABC): ...

class PasswordAuthCommand(AuthCommand):
    username: str
    password: str

class TokenAuthCommand(AuthCommand):
    token: str
    token_type: AuthTokenType

class UserAccountDTO(BaseModel):
    id: str
    name: str
    email: Optional[str] = None
    username: str
    photo: Optional[str] = None

    @classmethod
    def from_user_model(cls, user: UserAccount) -> "UserAccountDTO":
        return UserAccountDTO(
            id=user.id,
            name=user.name,
            email=user.email,
            username=user.username,
            photo=user.photo
        )

class UserIdentifier(BaseModel):
    id: str
    identifier_type: IdentifierType = IdentifierType.ID

class ChangeUserInfoCommand(BaseModel):
    id: UserIdentifier
    name: Optional[str] = None
    username: Optional[str] = None
    photo: Optional[str] = None

    def to_update_data(self) -> UserUpdateData:
        return UserUpdateData(
            name=self.name,
            username=self.username,
            photo=self.photo
        )

class ChangePasswordCommand(BaseModel):
    id: UserIdentifier
    new_password: str
    verification_code: str