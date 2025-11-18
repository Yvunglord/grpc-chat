import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE: _ClassVar[NotificationType]
    MENTION: _ClassVar[NotificationType]
    REACTION: _ClassVar[NotificationType]
    CHAT_INVITE: _ClassVar[NotificationType]
    FRIEND_REQUEST: _ClassVar[NotificationType]
    SYSTEM: _ClassVar[NotificationType]
MESSAGE: NotificationType
MENTION: NotificationType
REACTION: NotificationType
CHAT_INVITE: NotificationType
FRIEND_REQUEST: NotificationType
SYSTEM: NotificationType

class Notification(_message.Message):
    __slots__ = ("id", "user_id", "type", "title", "body", "data", "is_read", "created_at", "chat_id", "message_id", "sender_id")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_READ_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    user_id: str
    type: NotificationType
    title: str
    body: str
    data: _containers.ScalarMap[str, str]
    is_read: bool
    created_at: _timestamp_pb2.Timestamp
    chat_id: str
    message_id: str
    sender_id: str
    def __init__(self, id: _Optional[str] = ..., user_id: _Optional[str] = ..., type: _Optional[_Union[NotificationType, str]] = ..., title: _Optional[str] = ..., body: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ..., is_read: bool = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., chat_id: _Optional[str] = ..., message_id: _Optional[str] = ..., sender_id: _Optional[str] = ...) -> None: ...

class NotificationSubscription(_message.Message):
    __slots__ = ("user_id", "types")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    types: _containers.RepeatedScalarFieldContainer[NotificationType]
    def __init__(self, user_id: _Optional[str] = ..., types: _Optional[_Iterable[_Union[NotificationType, str]]] = ...) -> None: ...

class MarkReadRequest(_message.Message):
    __slots__ = ("success", "marked_count")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MARKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    marked_count: int
    def __init__(self, success: bool = ..., marked_count: _Optional[int] = ...) -> None: ...

class MarkReadResponse(_message.Message):
    __slots__ = ("success", "marked_count")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MARKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    marked_count: int
    def __init__(self, success: bool = ..., marked_count: _Optional[int] = ...) -> None: ...

class UnreadCountRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UnreadCountResponse(_message.Message):
    __slots__ = ("total_unread", "unread_by_type")
    class UnreadByTypeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TOTAL_UNREAD_FIELD_NUMBER: _ClassVar[int]
    UNREAD_BY_TYPE_FIELD_NUMBER: _ClassVar[int]
    total_unread: int
    unread_by_type: _containers.ScalarMap[str, int]
    def __init__(self, total_unread: _Optional[int] = ..., unread_by_type: _Optional[_Mapping[str, int]] = ...) -> None: ...
