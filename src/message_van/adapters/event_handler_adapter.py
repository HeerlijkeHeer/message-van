from collections.abc import AsyncGenerator

from message_van.domain.models.types import EventHandler


class EventHandlerAdapter:
    async def list(self) -> AsyncGenerator[EventHandler]:
        pass
