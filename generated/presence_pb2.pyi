import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[UserStatus]
    ONLINE: _ClassVar[UserStatus]
    OFFLINE: _ClassVar[UserStatus]
    AWAY: _ClassVar[UserStatus]
    DO_NOT_DISTURB: _ClassVar[UserStatus]
    CUSTOM: _ClassVar[UserStatus]
UNKNOWN: UserStatus
ONLINE: UserStatus
OFFLINE: UserStatus
AWAY: UserStatus
DO_NOT_DISTURB: UserStatus
CUSTOM: UserStatus

class PresenceUpdate(_message.Message):
    __slots__ = ("user_id", "status", "custom_status", "last_seen", "is_typing", "chat_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_STATUS_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_FIELD_NUMBER: _ClassVar[int]
    IS_TYPING_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    status: UserStatus
    custom_status: str
    last_seen: _timestamp_pb2.Timestamp
    is_typing: bool
    chat_id: str
    def __init__(self, user_id: _Optional[str] = ..., status: _Optional[_Union[UserStatus, str]] = ..., custom_status: _Optional[str] = ..., last_seen: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., is_typing: bool = ..., chat_id: _Optional[str] = ...) -> None: ...

class PresenceResponse(_message.Message):
    __slots__ = ("success", "message", "timestamp")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, success: bool = ..., message: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class OnlineUsersRequest(_message.Message):
    __slots__ = ("chat_id", "user_ids", "limit")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    limit: int
    def __init__(self, chat_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ..., limit: _Optional[int] = ...) -> None: ...

class OnlineUsersResponse(_message.Message):
    __slots__ = ("online_users", "total_count", "timestamp")
    ONLINE_USERS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    online_users: _containers.RepeatedCompositeFieldContainer[PresenceUpdate]
    total_count: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, online_users: _Optional[_Iterable[_Union[PresenceUpdate, _Mapping]]] = ..., total_count: _Optional[int] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StreamRequest(_message.Message):
    __slots__ = ("user_id", "chat_ids", "events")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    events: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., chat_ids: _Optional[_Iterable[str]] = ..., events: _Optional[_Iterable[str]] = ...) -> None: ...

class TypingUpdate(_message.Message):
    __slots__ = ("user_id", "chat_id", "is_typing")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_TYPING_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    chat_id: str
    is_typing: bool
    def __init__(self, user_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., is_typing: bool = ...) -> None: ...
