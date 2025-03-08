from typing import TYPE_CHECKING, Any, Awaitable, Callable

from message_van.domain.models.base import Command


if TYPE_CHECKING:
    from message_van.domain.models import MessageVan

    message_van_type = MessageVan
else:
    message_van_type = "MessageVan"


CommandHandler = Callable[[Command, message_van_type], Awaitable[Any | None]]
