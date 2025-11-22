from enum import Enum
from datetime import datetime
from typing import List, Dict, Any, Optional

class NotificationType(Enum):
    MESSAGE = 0
    MENTION = 1
    REACTION = 2
    CHAT_INVITE = 3
    FRIEND_REQUEST = 4
    SYSTEM = 5

class Notification():
     def __init__(
        self,
        user_id: str,
        notification_type: NotificationType,
        title: str,
        body: str,
        data: Optional[Dict[str, str]] = None,
        chat_id: Optional[str] = None,
        message_id: Optional[str] = None,
        sender_id: Optional[str] = None
    ):
        self.id = None,
        self.type = notification_type
        self.title = title
        self.body = body
        self.data = data or {}
        self.is_read = False
        self.created_at = datetime.utcnow()
        self.chat_id = chat_id
        self.message_id = message_id
        self.sender_id = sender_id
