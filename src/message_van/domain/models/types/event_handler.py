from typing import TYPE_CHECKING, Awaitable, Callable

from message_van.domain.models.base import Event


if TYPE_CHECKING:
    from message_van.domain.models import MessageVan

    message_van_type = MessageVan
else:
    message_van_type = "MessageVan"


EventHandler = Callable[[Event, "MessageVan"], Awaitable[None]]
