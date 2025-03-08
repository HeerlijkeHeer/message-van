from message_van.domain.models.base import Event
from message_van.domain.models.types import EventHandler
from message_van.domain.exceptions import UnknownHandlerError


class EventHandlers:
    def __init__(self, handler_map: dict[type[Event], list[EventHandler]]):
        self.handler_map = handler_map

    def get(self, event: Event) -> list[EventHandler]:
        event_type = type(event)

        return self._get(event_type)

    def _get(self, event_type: type[Event]) -> list[EventHandler]:
        try:
            return self.handler_map[event_type]
        except KeyError:
            raise UnknownHandlerError(event_type)
