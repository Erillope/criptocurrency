from src.user.core.domain.user_account import UserAccount
from abc import ABC, abstractmethod
from .dto import UserIdentifier

class GetUserRepository(ABC):
    @abstractmethod
    def get(self, identifier: UserIdentifier) -> UserAccount: ...

    @abstractmethod
    def exists(self, identifier: UserIdentifier) -> bool: ...