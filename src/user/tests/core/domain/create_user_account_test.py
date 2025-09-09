from unittest import TestCase
from src.user.core.domain.user_account import UserAccount
from src.user.core.domain.values import UserUpdateData
from src.user.core.domain.exceptions import UserAccountException
from .test_data import create_new_user_account_data, secondary_user_account_data, invalid_user_account_data

class TestCreateUserAccount(TestCase):
    def test_create_new_user_account(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        self.assertEqual(user.name, create_new_user_account_data["name"])
        self.assertEqual(user.username, create_new_user_account_data["username"])
    
    def test_create_user_account_with_invalid_name(self) -> None:
        with self.assertRaises(UserAccountException) as invalid_name_context:
            UserAccount.create(name=invalid_user_account_data["name"], username=create_new_user_account_data["username"])
        self.assertEqual(invalid_name_context.exception.code, 2)
    
    def test_create_user_account_with_invalid_username(self) -> None:
        with self.assertRaises(UserAccountException) as invalid_username_context:
            UserAccount.create(name=create_new_user_account_data["name"], username=invalid_user_account_data["username"])
        self.assertEqual(invalid_username_context.exception.code, 3)