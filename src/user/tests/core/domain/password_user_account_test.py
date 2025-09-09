from unittest import TestCase
from src.user.core.domain.user_account import UserAccount
from src.user.core.domain.exceptions import UserAccountException
from .test_data import create_new_user_account_data, user_account_data, invalid_user_account_data

class TestPasswordUserAccount(TestCase):
    def test_set_password(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        user.set_password(user_account_data["password"])
        self.assertIsNotNone(user.get_hashed_password())
    
    def test_set_invalid_password(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        with self.assertRaises(UserAccountException) as invalid_password_context:
            user.set_password(invalid_user_account_data["password"])
        self.assertEqual(invalid_password_context.exception.code, 6)
    
    def test_check_password(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        user.set_password(user_account_data["password"])
        self.assertTrue(user.check_password(user_account_data["password"]))
    
    def test_check_password_without_hashed_password(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        with self.assertRaises(UserAccountException) as without_password_context:
            user.check_password(user_account_data["password"])
        self.assertEqual(without_password_context.exception.code, 1)