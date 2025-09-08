from pydantic import BaseModel, PrivateAttr
from typing import Optional

class UserAccount(BaseModel):
    id: str
    name: str
    email: Optional[str] = None
    username: str
    photo: Optional[str] = None
    facebook: Optional[str] = None
    _hashed_password: Optional[str] = PrivateAttr(default=None)

    @classmethod
    def create(cls, *, name: str, username: str) -> "UserAccount":
        raise NotImplementedError("Method create not implemented")
    
    def check_password(self, password: str) -> bool:
        raise NotImplementedError("Method check_password not implemented")

    def get_hashed_password(self) -> Optional[str]:
        raise NotImplementedError("Method get_hashed_password not implemented")

    def save(self) -> None:
        raise NotImplementedError("Method save not implemented")

    def set_name(self, name: str) -> None:
        raise NotImplementedError("Method set_name not implemented")
    
    def set_email(self, email: str) -> None:
        raise NotImplementedError("Method set_email not implemented")

    def set_username(self, username: str) -> None:
        raise NotImplementedError("Method set_username not implemented")

    def set_password(self, password: str) -> None:
        raise NotImplementedError("Method set_password not implemented")

    def set_photo(self, photo: str) -> None:
        raise NotImplementedError("Method set_photo not implemented")

    def set_facebook(self, facebook: str) -> None:
        raise NotImplementedError("Method set_facebook not implemented")