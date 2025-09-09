from pydantic import BaseModel, PrivateAttr, model_validator
from typing import Optional
from uuid import uuid4
from .exceptions import UserAccountException
from .values import UserUpdateData
from .validators import UserAccountValidator
from src.user.core.util import PasswordChecker, PasswordHasher

class UserAccount(BaseModel):
    id: str
    name: str
    email: Optional[str] = None
    username: str
    photo: Optional[str] = None
    facebook: Optional[str] = None
    _hashed_password: Optional[str] = PrivateAttr(default=None)
    _password_checker: PasswordChecker = PrivateAttr(default=PasswordChecker())
    _password_hasher: PasswordHasher = PrivateAttr(default=PasswordHasher())
    _validator: UserAccountValidator = PrivateAttr(default=UserAccountValidator())

    @classmethod
    def create(cls, *, name: str, username: str) -> "UserAccount":
        return cls(
            id=str(uuid4()),
            name=name,
            username=username
        )
    
    @model_validator(mode="after")
    def _validate(self) -> "UserAccount":
        self._validator.validate_user(self)
        return self
    
    def check_password(self, password: str) -> bool:
        if self._hashed_password is None:
            raise UserAccountException.without_password(self.username)
        return self._password_checker.check(self._hashed_password, password)

    def get_hashed_password(self) -> Optional[str]:
        return self._hashed_password

    def save(self) -> None:
        raise NotImplementedError("Method save not implemented")
    
    def set_password(self, password: str) -> None:
        if not self._validator.validate_password(password):
            raise UserAccountException.invalid_password()
        self._hashed_password = self._password_hasher.hash(password)

    def update(self, data: UserUpdateData) -> None:
        for field, value in data.model_dump(exclude_none=True).items():
            if field != "password":
                setattr(self, field, value)
        if data.password is not None:
            self.set_password(data.password)
        self._validator.validate_user(self)