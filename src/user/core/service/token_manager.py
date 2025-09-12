from abc import ABC, abstractmethod

class TokenManager(ABC):
    @abstractmethod
    def refresh(self, refresh_token: str) -> str: ...

    @abstractmethod
    def invalidate(self, access_token: str) -> None: ...