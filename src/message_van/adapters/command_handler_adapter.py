from collections.abc import AsyncGenerator

from message_van.domain.models.types import CommandHandler


class CommandHandlerAdapter:
    async def list(self) -> AsyncGenerator[CommandHandler]:
        pass
