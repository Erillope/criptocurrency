from abc import ABC, abstractmethod
from .dto import AuthCommand, UserAccountDTO
from typing import Generic, TypeVar

Strategy = TypeVar('Strategy', bound=AuthCommand)

class AuthStrategy(ABC, Generic[Strategy]):
    @abstractmethod
    def authenticate(self, auth_command: Strategy) -> UserAccountDTO: ...