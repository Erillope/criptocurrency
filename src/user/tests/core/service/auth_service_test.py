from unittest import TestCase
from src.user.core.service.auth_service import AuthService
from src.user.tests.core.stubs import StubPasswordAuthStrategy, StubTokenAuthStrategy, StubTokenManager
from src.user.core.service.dto import PasswordAuthCommand, TokenAuthCommand, AuthTokenType
from src.user.core.service.exceptions import UserServiceException
from enum import Enum

class TestAuthService(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.password_auth_strategy = StubPasswordAuthStrategy()
        cls.google_token_auth_strategy = StubTokenAuthStrategy()
        cls.facebook_token_auth_strategy = StubTokenAuthStrategy()
        cls.token_manager = StubTokenManager()
        cls.token_auth_strategies = {
            AuthTokenType.GOOGLE: cls.google_token_auth_strategy,
            AuthTokenType.FACEBOOK: cls.facebook_token_auth_strategy
        }
        cls.auth_service = AuthService(
            password_auth=cls.password_auth_strategy,
            token_auth_strategies=cls.token_auth_strategies,
            token_manager=cls.token_manager
        )
    
    def test_authenticate_with_password(self) -> None:
        command = PasswordAuthCommand(username="testuser", password="testpass")
        user_dto = self.auth_service.authenticate(command)
        self.assertEqual(user_dto.username, "testuser")
    
    def test_authenticate_with_token(self) -> None:
        command = TokenAuthCommand(token="testtoken", token_type=AuthTokenType.GOOGLE)
        user_dto = self.auth_service.authenticate(command)
        self.assertEqual(user_dto.username, command.token)
    
    def test_authenticate_with_unknown_command(self) -> None:
        updated_auth_token_type = Enum("AuthTokenType", { "NEW": "new" })
        command = updated_auth_token_type.NEW
        with self.assertRaises(UserServiceException) as no_strategy_found_context:
            self.auth_service.authenticate(command)
        self.assertEqual(no_strategy_found_context.exception.code, 8)
    
    def test_authenticate_without_strategies(self) -> None:
        auth_service = AuthService(
            password_auth=self.password_auth_strategy,
            token_auth_strategies={},
            token_manager=self.token_manager
        )
        command = TokenAuthCommand(token="testtoken", token_type=AuthTokenType.GOOGLE)
        with self.assertRaises(UserServiceException) as no_strategy_found_context:
            auth_service.authenticate(command)
        self.assertEqual(no_strategy_found_context.exception.code, 8)