from pydantic import BaseModel
import re
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user_account import UserAccount
from .exceptions import UserAccountException

class UserAccountValidator(BaseModel):
    name_regex: str = r"^[a-zA-Z\s]{1,50}$" # Only letters and spaces, max length 50
    username_regex: str = r"^[a-zA-Z0-9_]{3,30}$" # Alphanumeric and underscores, length 3-30
    email_regex: str = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" # Basic email pattern
    photo_regex: str = r"^(http|https):\/\/.*\.(jpg|jpeg|png|gif)$" # URL ending with image extensions
    password_regex: str = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"  # Minimum eight characters, at least one letter and one number

    def validate_name(self, name: str) -> bool:
        return bool(re.match(self.name_regex, name))
    
    def validate_username(self, username: str) -> bool:
        return bool(re.match(self.username_regex, username))
    
    def validate_email(self, email: str) -> bool:
        return bool(re.match(self.email_regex, email))
    
    def validate_photo(self, photo: str) -> bool:
        return bool(re.match(self.photo_regex, photo))
    
    def validate_password(self, password: str) -> bool:
        return bool(re.match(self.password_regex, password))
    
    def validate_user(self, user: "UserAccount") -> None:
        if not self.validate_name(user.name):
            raise UserAccountException.invalid_name(user.name)
        if not self.validate_username(user.username):
            raise UserAccountException.invalid_username(user.username)
        if user.email and not self.validate_email(user.email):
            raise UserAccountException.invalid_email(user.email)
        if user.photo and not self.validate_photo(user.photo):
            raise UserAccountException.invalid_photo(user.photo)