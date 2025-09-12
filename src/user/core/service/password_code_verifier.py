from abc import ABC, abstractmethod

class PasswordCodeVerifier(ABC):
    @abstractmethod
    def verify(self, code: str, user_id: str) -> bool: ...

    @abstractmethod
    def send_code(self, user_id: str) -> None: ...