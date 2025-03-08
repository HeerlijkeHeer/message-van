from message_van.domain.models import Command, Event


Message = Command | Event
