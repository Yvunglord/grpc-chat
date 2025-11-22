from datetime import datetime
from enum import Enum
from typing import Optional

class UserStatus(Enum):
    UNKNOWN = 0
    ONLINE = 1 
    OFFLINE = 2 
    AWAY = 3 
    DO_NOT_DISTURB = 4 
    CUSTOM = 5 

class PresenceState:
    def __init__(
        self,
        user_id: str,
        status: UserStatus = UserStatus.OFFLINE,
        custom_status: Optional[str] = None,
        last_seen: Optional[datetime] = None,
        is_typing: bool = False,
        chat_id: Optional[str] = None
    ):
        self.user_id = user_id
        self.status = status
        self.custom_status = custom_status
        self.last_seen = last_seen
        self.is_typing = is_typing
        self.chat_id = chat_id