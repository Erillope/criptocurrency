from abc import ABC, abstractmethod
from typing import Type, Dict, List, Generic, TypeVar, Any

E = TypeVar("E", bound="Event")

class Event(ABC):
    def dispatch(self) -> None:
        EventDispatcher.dispatch_event(self)

class EventListener(ABC, Generic[E]):
    listen_to: Type[E]

    def __init__(self) -> None:
        EventDispatcher.register_listener(self)

    @abstractmethod
    def handle_event(self, event: E) -> None: ...

class EventDispatcher:
    listeners: Dict[Type[Event], List[EventListener[Any]]] = {}

    @classmethod
    def register_listener(cls, listener: EventListener[E]) -> None:
        cls.listeners.setdefault(listener.listen_to, []).append(listener)

    @classmethod
    def dispatch_event(cls, event: Event) -> None:
        listeners = cls.listeners.get(type(event), [])
        for listener in listeners:
            listener.handle_event(event)