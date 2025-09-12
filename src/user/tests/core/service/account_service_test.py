from unittest import TestCase
from src.user.core.service.auth_service import UserAccountService
from src.user.tests.core.stubs import StubPasswordRegisterStrategy, StubTokenRegisterStrategy, StubGetUserRepository, StubPasswordCodeVerifier
from src.user.core.service.dto import (PasswordAuthCommand, TokenAuthCommand, AuthTokenType, UserIdentifier,
                                       ChangeUserInfoCommand, ChangePasswordCommand)
from enum import Enum
from src.user.core.service.exceptions import UserServiceException

class TestUserAccountService(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.password_register_strategy = StubPasswordRegisterStrategy()
        cls.google_token_register_strategy = StubTokenRegisterStrategy()
        cls.facebook_token_register_strategy = StubTokenRegisterStrategy()
        cls.get_user_repository = StubGetUserRepository()
        cls.password_code_verifier = StubPasswordCodeVerifier()
        cls.token_register_strategies = {
            AuthTokenType.GOOGLE: cls.google_token_register_strategy,
            AuthTokenType.FACEBOOK: cls.facebook_token_register_strategy
        }
        cls.user_account_service = UserAccountService(
            password_register=cls.password_register_strategy,
            token_register_strategies=cls.token_register_strategies,
            get_user_repository=cls.get_user_repository,
            password_code_verifier=cls.password_code_verifier
        )

    def test_register_with_password(self) -> None:
        command = PasswordAuthCommand(username="newuser", password="newpass")
        user_dto = self.user_account_service.register(command)
        self.assertEqual(user_dto.username, "newuser")
    
    def test_register_with_token(self) -> None:
        command = TokenAuthCommand(token="newtoken", token_type=AuthTokenType.GOOGLE)
        user_dto = self.user_account_service.register(command)
        self.assertEqual(user_dto.username, command.token)
    
    def test_register_with_unknown_command(self) -> None:
        updated_auth_token_type = Enum("AuthTokenType", { "NEW": "new" })
        command = updated_auth_token_type.NEW
        with self.assertRaises(UserServiceException) as no_strategy_found_context:
            self.user_account_service.register(command)
        self.assertEqual(no_strategy_found_context.exception.code, 8)
    
    def test_register_without_strategies(self) -> None:
        user_account_service = UserAccountService(
            password_register=self.password_register_strategy,
            token_register_strategies={},
            get_user_repository=self.get_user_repository,
            password_code_verifier=self.password_code_verifier
        )
        command = TokenAuthCommand(token="newtoken", token_type=AuthTokenType.GOOGLE)
        with self.assertRaises(UserServiceException) as no_strategy_found_context:
            user_account_service.register(command)
        self.assertEqual(no_strategy_found_context.exception.code, 8)
    
    def test_change_user_info(self) -> None:
        command = ChangeUserInfoCommand(id=UserIdentifier(id="dummy_id"), name="Updated User", username="updateduser")
        user_dto = self.user_account_service.change_user_info(command)
        self.assertEqual(user_dto.name, "Updated User")
        self.assertEqual(user_dto.username, "updateduser")
    
    def test_change_password(self) -> None:
        command = ChangePasswordCommand(id=UserIdentifier(id="dummy_id"), new_password="Newpassword1", verification_code="valid_code")
        self.user_account_service.change_password(command)
        # If no exception is raised, the test is successful
    
    def test_change_password_with_invalid_code(self) -> None:
        command = ChangePasswordCommand(id=UserIdentifier(id="dummy_id"), new_password="Newpassword1", verification_code="invalid_code")
        self.password_code_verifier.verify_value = False
        with self.assertRaises(UserServiceException) as invalid_code_context:
            self.user_account_service.change_password(command)
        self.assertEqual(invalid_code_context.exception.code, 10)
        self.password_code_verifier.verify_value = True  # Reset for other tests
    
    def test_get_user_data(self) -> None:
        identifier = UserIdentifier(id="existinguser")
        user_dto = self.user_account_service.get_user_data(identifier)
        self.assertEqual(user_dto.id, "existinguser")
    
    def test_get_user_data_not_found(self) -> None:
        identifier = UserIdentifier(id="nonexistentuser")
        self.get_user_repository.exists_value = False
        with self.assertRaises(UserServiceException) as user_not_found_context:
            self.user_account_service.get_user_data(identifier)
        self.assertEqual(user_not_found_context.exception.code, 9)
        self.get_user_repository.exists_value = True  # Reset for other tests