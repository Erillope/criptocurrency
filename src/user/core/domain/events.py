from src.common.events import Event
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user_account import UserAccount

class UserCreated(Event):
    def __init__(self, user: "UserAccount") -> None:
        self.user = user
        super().__init__()