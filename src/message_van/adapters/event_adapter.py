from collections.abc import AsyncGenerator
from pathlib import Path

from message_van.domain.models.base import Event


class EventAdapter:
    def __init__(self, path: Path):
        self.path = path

    async def list(self) -> AsyncGenerator[Event]:
        pass
