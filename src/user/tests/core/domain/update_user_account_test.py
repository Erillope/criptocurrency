from unittest import TestCase
from src.user.core.domain.user_account import UserAccount
from src.user.core.domain.values import UserUpdateData
from src.user.core.domain.exceptions import UserAccountException
from .test_data import create_new_user_account_data, secondary_user_account_data, invalid_user_account_data

class TestCreateUserAccount(TestCase):    
    def test_update_user_account_data(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        update_data = UserUpdateData(**secondary_user_account_data)
        user.update(update_data)
        self.assertEqual(user.name, secondary_user_account_data["name"])
        self.assertEqual(user.username, secondary_user_account_data["username"])
        self.assertEqual(user.email, secondary_user_account_data["email"])
        self.assertEqual(user.photo, secondary_user_account_data["photo"])
    
    def test_update_user_account_with_invalid_name(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        update_data = UserUpdateData(name=invalid_user_account_data["name"])
        with self.assertRaises(UserAccountException) as invalid_name_context:
            user.update(update_data)
        self.assertEqual(invalid_name_context.exception.code, 2)
    
    def test_update_user_account_with_invalid_username(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        update_data = UserUpdateData(username=invalid_user_account_data["username"])
        with self.assertRaises(UserAccountException) as invalid_username_context:
            user.update(update_data)
        self.assertEqual(invalid_username_context.exception.code, 3)
    
    def test_update_user_account_with_invalid_email(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        update_data = UserUpdateData(email=invalid_user_account_data["email"])
        with self.assertRaises(UserAccountException) as invalid_email_context:
            user.update(update_data)
        self.assertEqual(invalid_email_context.exception.code, 4)
    
    def test_update_user_account_with_invalid_photo(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        update_data = UserUpdateData(photo=invalid_user_account_data["photo"])
        with self.assertRaises(UserAccountException) as invalid_photo_context:
            user.update(update_data)
        self.assertEqual(invalid_photo_context.exception.code, 5)