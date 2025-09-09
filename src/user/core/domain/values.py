from pydantic import BaseModel
from typing import Optional

class UserUpdateData(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    username: Optional[str] = None
    photo: Optional[str] = None
    facebook: Optional[str] = None
    password: Optional[str] = None