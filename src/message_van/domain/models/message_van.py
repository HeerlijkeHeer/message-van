from asyncio import create_task, gather
from types import TracebackType
from typing import Any

from message_van.domain.models.base import Command, Event, Message

from . import CommandHandlers, EventHandlers, UnitOfWork


class MessageVan:
    uow: UnitOfWork

    def __init__(
        self,
        command_handlers: CommandHandlers,
        event_handlers: EventHandlers,
        unit_of_work: UnitOfWork,
    ):
        self.command_handlers = command_handlers
        self.event_handlers = event_handlers
        self.unit_of_work = unit_of_work

    async def __aenter__(self) -> "MessageVan":
        self.uow = await self.unit_of_work.__aenter__()

        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> bool | None:
        await self.unit_of_work.__aexit__(exc_type, exc_val, exc_tb)

    async def publish(self, message: Message) -> Any | None:
        if isinstance(message, Command):
            return await self.publish_command(message)

        await self.publish_event(message)

    async def publish_command(self, command: Command) -> Any:
        handler = self.command_handlers.get(command)

        return await handler(command, self)

    async def publish_event(self, event: Event) -> None:
        tasks = [
            create_task(handler(event, self))
            for handler in self.event_handlers.get(event)
        ]

        await gather(*tasks)

    def _get_handlers(self, message_type: type[Message]):
        if issubclass(message_type, Event):
            return self.event_handlers
        else:
            return self.command_handlers
