from unittest import TestCase
from src.user.core.util.password import PasswordChecker, PasswordHasher

class TestPassword(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.password_hasher = PasswordHasher()
        self.password_checker = PasswordChecker()
        self.plain_password = "SecurePassword123!"
        self.wrong_password = "WrongPassword456!"
    
    def test_hash_password(self) -> None:
        hashed_password = self.password_hasher.hash(self.plain_password)
        self.assertNotEqual(hashed_password, self.plain_password)

    def test_check_password_success(self) -> None:
        hashed_password = self.password_hasher.hash(self.plain_password)
        self.assertTrue(self.password_checker.check(hashed_password, self.plain_password))
    
    def test_check_password_failure(self) -> None:
        hashed_password = self.password_hasher.hash(self.plain_password)
        self.assertFalse(self.password_checker.check(hashed_password, self.wrong_password))