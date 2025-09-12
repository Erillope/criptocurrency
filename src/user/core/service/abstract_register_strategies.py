from abc import ABC, abstractmethod
from .dto import AuthCommand, UserAccountDTO
from typing import Generic, TypeVar

Strategy = TypeVar("Strategy", bound=AuthCommand)

class RegisterStrategy(ABC, Generic[Strategy]):
    @abstractmethod
    def register(self, command: Strategy) -> UserAccountDTO: ...