from unittest import TestCase
from src.user.core.domain.validators import UserAccountValidator
from .test_data import invalid_user_account_data, user_account_data

class TestUserAccountValidator(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.validator = UserAccountValidator()
    
    def test_validate_name(self) -> None:
        self.assertTrue(self.validator.validate_name(user_account_data["name"]))
    
    def test_validate_username(self) -> None:
        self.assertTrue(self.validator.validate_username(user_account_data["username"]))
    
    def test_validate_email(self) -> None:
        self.assertTrue(self.validator.validate_email(user_account_data["email"]))
    
    def test_validate_photo(self) -> None:
        self.assertTrue(self.validator.validate_photo(user_account_data["photo"]))
    
    def test_validate_password(self) -> None:
        self.assertTrue(self.validator.validate_password(user_account_data["password"]))
    
    def test_invalid_name(self) -> None:
        self.assertFalse(self.validator.validate_name(invalid_user_account_data["name"]))
    
    def test_invalid_username(self) -> None:
        self.assertFalse(self.validator.validate_username(invalid_user_account_data["username"]))
    
    def test_invalid_email(self) -> None:
        self.assertFalse(self.validator.validate_email(invalid_user_account_data["email"]))
    
    def test_invalid_photo(self) -> None:
        self.assertFalse(self.validator.validate_photo(invalid_user_account_data["photo"]))
    
    def test_invalid_password(self) -> None:
        self.assertFalse(self.validator.validate_password(invalid_user_account_data["password"]))