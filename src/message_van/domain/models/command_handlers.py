from message_van.domain.models.base import Command
from message_van.domain.models.types import CommandHandler
from message_van.domain.exceptions import UnknownHandlerError


class CommandHandlers:
    def __init__(self, handler_map: dict[type[Command], CommandHandler]):
        self.handler_map = handler_map

    def get(self, command: Command) -> CommandHandler:
        command_type = type(command)

        return self._get(command_type)

    def _get(self, command_type: type[Command]) -> CommandHandler:
        try:
            return self.handler_map[command_type]
        except KeyError:
            raise UnknownHandlerError(command_type)
