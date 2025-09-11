from unittest import TestCase
from src.user.core.domain.user_account import UserAccount
from src.user.core.domain.exceptions import UserAccountException
from .test_data import create_new_user_account_data, user_account_data

class TestSaveUserAccount(TestCase):
    def test_save_user_account(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        user.set_password(user_account_data["password"])
        user.save()  # Should not raise any exception

    def test_cannot_save_user_account_without_email_facebook_or_password(self) -> None:
        user = UserAccount.create(**create_new_user_account_data)
        with self.assertRaises(UserAccountException) as without_account_context:
            user.save()
        self.assertEqual(without_account_context.exception.code, 7)