from pydantic import BaseModel
from typing import Optional
from enum import Enum
from abc import ABC

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

class UserIdentifier(BaseModel):
    id: str
    identifier_type: IdentifierType

class ChangeUserInfoCommand(BaseModel):
    id: UserIdentifier
    name: Optional[str] = None
    username: Optional[str] = None
    photo: Optional[str] = None

class ChangePasswordCommand(BaseModel):
    new_password: str
    verification_code: str