import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
import presence_pb2 as _presence_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEXT: _ClassVar[MessageType]
    IMAGE: _ClassVar[MessageType]
    FILE: _ClassVar[MessageType]
    SYSTEM: _ClassVar[MessageType]
    VOICE: _ClassVar[MessageType]
    VIDEO: _ClassVar[MessageType]

class MessageStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SENDING: _ClassVar[MessageStatus]
    SENT: _ClassVar[MessageStatus]
    DELIVERED: _ClassVar[MessageStatus]
    READ: _ClassVar[MessageStatus]
    FAILED: _ClassVar[MessageStatus]

class ChatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DIRECT: _ClassVar[ChatType]
    GROUP: _ClassVar[ChatType]
    CHANNEL: _ClassVar[ChatType]

class ChatEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MESSAGE_SENT: _ClassVar[ChatEventType]
    MESSAGE_EDITED: _ClassVar[ChatEventType]
    MESSAGE_DELETED: _ClassVar[ChatEventType]
    USER_JOINED: _ClassVar[ChatEventType]
    USER_LEFT: _ClassVar[ChatEventType]
    USER_TYPING: _ClassVar[ChatEventType]
    USER_STOPPED_TYPING: _ClassVar[ChatEventType]
    CHAT_UPDATED: _ClassVar[ChatEventType]
TEXT: MessageType
IMAGE: MessageType
FILE: MessageType
SYSTEM: MessageType
VOICE: MessageType
VIDEO: MessageType
SENDING: MessageStatus
SENT: MessageStatus
DELIVERED: MessageStatus
READ: MessageStatus
FAILED: MessageStatus
DIRECT: ChatType
GROUP: ChatType
CHANNEL: ChatType
MESSAGE_SENT: ChatEventType
MESSAGE_EDITED: ChatEventType
MESSAGE_DELETED: ChatEventType
USER_JOINED: ChatEventType
USER_LEFT: ChatEventType
USER_TYPING: ChatEventType
USER_STOPPED_TYPING: ChatEventType
CHAT_UPDATED: ChatEventType

class CreateChatRequest(_message.Message):
    __slots__ = ("name", "participant_ids", "chat_type", "description", "avatar_url")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    CHAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    name: str
    participant_ids: _containers.RepeatedScalarFieldContainer[str]
    chat_type: ChatType
    description: str
    avatar_url: str
    def __init__(self, name: _Optional[str] = ..., participant_ids: _Optional[_Iterable[str]] = ..., chat_type: _Optional[_Union[ChatType, str]] = ..., description: _Optional[str] = ..., avatar_url: _Optional[str] = ...) -> None: ...

class GetChatRequest(_message.Message):
    __slots__ = ("chat_id",)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    def __init__(self, chat_id: _Optional[str] = ...) -> None: ...

class GetUserChatsRequest(_message.Message):
    __slots__ = ("user_id", "limit", "offset", "include_archived")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    limit: int
    offset: int
    include_archived: bool
    def __init__(self, user_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., include_archived: bool = ...) -> None: ...

class GetUserChatsResponse(_message.Message):
    __slots__ = ("chats", "total_count", "has_more", "next_offset")
    CHATS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    chats: _containers.RepeatedCompositeFieldContainer[ChatResponse]
    total_count: int
    has_more: bool
    next_offset: str
    def __init__(self, chats: _Optional[_Iterable[_Union[ChatResponse, _Mapping]]] = ..., total_count: _Optional[int] = ..., has_more: bool = ..., next_offset: _Optional[str] = ...) -> None: ...

class AddParticipantsRequest(_message.Message):
    __slots__ = ("chat_id", "user_ids", "added_by")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    ADDED_BY_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    added_by: str
    def __init__(self, chat_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ..., added_by: _Optional[str] = ...) -> None: ...

class RemoveParticipantsRequest(_message.Message):
    __slots__ = ("chat_id", "user_ids", "removed_by")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_IDS_FIELD_NUMBER: _ClassVar[int]
    REMOVED_BY_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_ids: _containers.RepeatedScalarFieldContainer[str]
    removed_by: str
    def __init__(self, chat_id: _Optional[str] = ..., user_ids: _Optional[_Iterable[str]] = ..., removed_by: _Optional[str] = ...) -> None: ...

class LeaveChatRequest(_message.Message):
    __slots__ = ("chat_id", "user_id")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_id: str
    def __init__(self, chat_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class LeaveChatResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class ChatResponse(_message.Message):
    __slots__ = ("chat_id", "name", "description", "chat_type", "participant_ids", "participants", "created_by", "avatar_url", "created_at", "updated_at", "last_message", "unread_count", "is_archived", "settings")
    class SettingsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CHAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANT_IDS_FIELD_NUMBER: _ClassVar[int]
    PARTICIPANTS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_URL_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UNREAD_COUNT_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    name: str
    description: str
    chat_type: ChatType
    participant_ids: _containers.RepeatedScalarFieldContainer[str]
    participants: _containers.RepeatedCompositeFieldContainer[ChatParticipant]
    created_by: str
    avatar_url: str
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    last_message: MessageResponse
    unread_count: int
    is_archived: bool
    settings: _containers.ScalarMap[str, str]
    def __init__(self, chat_id: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., chat_type: _Optional[_Union[ChatType, str]] = ..., participant_ids: _Optional[_Iterable[str]] = ..., participants: _Optional[_Iterable[_Union[ChatParticipant, _Mapping]]] = ..., created_by: _Optional[str] = ..., avatar_url: _Optional[str] = ..., created_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_message: _Optional[_Union[MessageResponse, _Mapping]] = ..., unread_count: _Optional[int] = ..., is_archived: bool = ..., settings: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ChatParticipant(_message.Message):
    __slots__ = ("user_id", "role", "joined_at", "last_read_at")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    JOINED_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_AT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role: str
    joined_at: _timestamp_pb2.Timestamp
    last_read_at: _timestamp_pb2.Timestamp
    def __init__(self, user_id: _Optional[str] = ..., role: _Optional[str] = ..., joined_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., last_read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SendMessageRequest(_message.Message):
    __slots__ = ("chat_id", "sender_id", "content", "message_type", "reply_to_message_id", "metadata")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    sender_id: str
    content: str
    message_type: MessageType
    reply_to_message_id: str
    metadata: _containers.ScalarMap[str, str]
    def __init__(self, chat_id: _Optional[str] = ..., sender_id: _Optional[str] = ..., content: _Optional[str] = ..., message_type: _Optional[_Union[MessageType, str]] = ..., reply_to_message_id: _Optional[str] = ..., metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class EditMessageRequest(_message.Message):
    __slots__ = ("message_id", "chat_id", "user_id", "new_content", "updated_metadata")
    class UpdatedMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTENT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_METADATA_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    chat_id: str
    user_id: str
    new_content: str
    updated_metadata: _containers.ScalarMap[str, str]
    def __init__(self, message_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., user_id: _Optional[str] = ..., new_content: _Optional[str] = ..., updated_metadata: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ("message_id", "chat_id", "user_id", "for_everyone")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    FOR_EVERYONE_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    chat_id: str
    user_id: str
    for_everyone: bool
    def __init__(self, message_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., user_id: _Optional[str] = ..., for_everyone: bool = ...) -> None: ...

class DeleteMessageResponse(_message.Message):
    __slots__ = ("success", "deleted_message_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DELETED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    deleted_message_id: str
    def __init__(self, success: bool = ..., deleted_message_id: _Optional[str] = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ("message_id", "chat_id")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    chat_id: str
    def __init__(self, message_id: _Optional[str] = ..., chat_id: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("message_id", "chat_id", "sender_id", "content", "message_type", "status", "timestamp", "edited_at", "reply_to_message_id", "reply_to_message", "metadata", "read_by", "delivered_to")
    class MetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    SENDER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EDITED_AT_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    READ_BY_FIELD_NUMBER: _ClassVar[int]
    DELIVERED_TO_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    chat_id: str
    sender_id: str
    content: str
    message_type: MessageType
    status: MessageStatus
    timestamp: _timestamp_pb2.Timestamp
    edited_at: _timestamp_pb2.Timestamp
    reply_to_message_id: str
    reply_to_message: MessageResponse
    metadata: _containers.ScalarMap[str, str]
    read_by: _containers.RepeatedScalarFieldContainer[str]
    delivered_to: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, message_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., sender_id: _Optional[str] = ..., content: _Optional[str] = ..., message_type: _Optional[_Union[MessageType, str]] = ..., status: _Optional[_Union[MessageStatus, str]] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., edited_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., reply_to_message_id: _Optional[str] = ..., reply_to_message: _Optional[_Union[MessageResponse, _Mapping]] = ..., metadata: _Optional[_Mapping[str, str]] = ..., read_by: _Optional[_Iterable[str]] = ..., delivered_to: _Optional[_Iterable[str]] = ...) -> None: ...

class GetChatHistoryRequest(_message.Message):
    __slots__ = ("chat_id", "limit", "before_message_id", "after_message_id", "since", "until", "message_types")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    BEFORE_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    AFTER_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    limit: int
    before_message_id: str
    after_message_id: str
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    message_types: _containers.RepeatedScalarFieldContainer[MessageType]
    def __init__(self, chat_id: _Optional[str] = ..., limit: _Optional[int] = ..., before_message_id: _Optional[str] = ..., after_message_id: _Optional[str] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message_types: _Optional[_Iterable[_Union[MessageType, str]]] = ...) -> None: ...

class ChatHistoryResponse(_message.Message):
    __slots__ = ("messages", "has_more", "next_before_message_id", "next_after_message_id", "total_count")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    NEXT_BEFORE_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageResponse]
    has_more: bool
    next_before_message_id: str
    next_after_message_id: str
    total_count: int
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageResponse, _Mapping]]] = ..., has_more: bool = ..., next_before_message_id: _Optional[str] = ..., next_after_message_id: _Optional[str] = ..., total_count: _Optional[int] = ...) -> None: ...

class SearchMessagesRequest(_message.Message):
    __slots__ = ("query", "chat_id", "user_id", "limit", "offset", "message_types", "since", "until")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SINCE_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    query: str
    chat_id: str
    user_id: str
    limit: int
    offset: int
    message_types: _containers.RepeatedScalarFieldContainer[MessageType]
    since: _timestamp_pb2.Timestamp
    until: _timestamp_pb2.Timestamp
    def __init__(self, query: _Optional[str] = ..., chat_id: _Optional[str] = ..., user_id: _Optional[str] = ..., limit: _Optional[int] = ..., offset: _Optional[int] = ..., message_types: _Optional[_Iterable[_Union[MessageType, str]]] = ..., since: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., until: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SearchMessagesResponse(_message.Message):
    __slots__ = ("messages", "total_count", "has_more", "next_offset")
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_COUNT_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    NEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[MessageResponse]
    total_count: int
    has_more: bool
    next_offset: str
    def __init__(self, messages: _Optional[_Iterable[_Union[MessageResponse, _Mapping]]] = ..., total_count: _Optional[int] = ..., has_more: bool = ..., next_offset: _Optional[str] = ...) -> None: ...

class MarkReadRequest(_message.Message):
    __slots__ = ("chat_id", "user_id", "up_to_message_id", "read_at")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    UP_TO_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_id: str
    up_to_message_id: str
    read_at: _timestamp_pb2.Timestamp
    def __init__(self, chat_id: _Optional[str] = ..., user_id: _Optional[str] = ..., up_to_message_id: _Optional[str] = ..., read_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class MarkReadResponse(_message.Message):
    __slots__ = ("success", "marked_count", "last_read_message_id")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MARKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    LAST_READ_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    success: bool
    marked_count: int
    last_read_message_id: str
    def __init__(self, success: bool = ..., marked_count: _Optional[int] = ..., last_read_message_id: _Optional[str] = ...) -> None: ...

class MarkDeliveredRequest(_message.Message):
    __slots__ = ("chat_id", "user_id", "message_ids")
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    user_id: str
    message_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, chat_id: _Optional[str] = ..., user_id: _Optional[str] = ..., message_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class MarkDeliveredResponse(_message.Message):
    __slots__ = ("success", "marked_count")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MARKED_COUNT_FIELD_NUMBER: _ClassVar[int]
    success: bool
    marked_count: int
    def __init__(self, success: bool = ..., marked_count: _Optional[int] = ...) -> None: ...

class UnreadCountRequest(_message.Message):
    __slots__ = ("user_id", "chat_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., chat_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class UnreadCountResponse(_message.Message):
    __slots__ = ("total_unread", "unread_by_chat")
    class UnreadByChatEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    TOTAL_UNREAD_FIELD_NUMBER: _ClassVar[int]
    UNREAD_BY_CHAT_FIELD_NUMBER: _ClassVar[int]
    total_unread: int
    unread_by_chat: _containers.ScalarMap[str, int]
    def __init__(self, total_unread: _Optional[int] = ..., unread_by_chat: _Optional[_Mapping[str, int]] = ...) -> None: ...

class StreamMessagesRequest(_message.Message):
    __slots__ = ("user_id", "chat_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_id: _Optional[str] = ..., chat_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class StreamChatEventsRequest(_message.Message):
    __slots__ = ("user_id", "chat_ids", "event_types")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_IDS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPES_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    chat_ids: _containers.RepeatedScalarFieldContainer[str]
    event_types: _containers.RepeatedScalarFieldContainer[ChatEventType]
    def __init__(self, user_id: _Optional[str] = ..., chat_ids: _Optional[_Iterable[str]] = ..., event_types: _Optional[_Iterable[_Union[ChatEventType, str]]] = ...) -> None: ...

class StreamMessage(_message.Message):
    __slots__ = ("new_message", "edited_message", "deleted_message_id", "typing_update", "status_update")
    NEW_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EDITED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPING_UPDATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    new_message: MessageResponse
    edited_message: MessageResponse
    deleted_message_id: str
    typing_update: _presence_pb2.TypingUpdate
    status_update: MessageStatusUpdate
    def __init__(self, new_message: _Optional[_Union[MessageResponse, _Mapping]] = ..., edited_message: _Optional[_Union[MessageResponse, _Mapping]] = ..., deleted_message_id: _Optional[str] = ..., typing_update: _Optional[_Union[_presence_pb2.TypingUpdate, _Mapping]] = ..., status_update: _Optional[_Union[MessageStatusUpdate, _Mapping]] = ...) -> None: ...

class ChatEvent(_message.Message):
    __slots__ = ("type", "chat_id", "timestamp", "message", "user_id", "typing_user_id", "chat_update")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    TYPING_USER_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_UPDATE_FIELD_NUMBER: _ClassVar[int]
    type: ChatEventType
    chat_id: str
    timestamp: _timestamp_pb2.Timestamp
    message: MessageResponse
    user_id: str
    typing_user_id: str
    chat_update: ChatResponse
    def __init__(self, type: _Optional[_Union[ChatEventType, str]] = ..., chat_id: _Optional[str] = ..., timestamp: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[MessageResponse, _Mapping]] = ..., user_id: _Optional[str] = ..., typing_user_id: _Optional[str] = ..., chat_update: _Optional[_Union[ChatResponse, _Mapping]] = ...) -> None: ...

class MessageStatusUpdate(_message.Message):
    __slots__ = ("message_id", "chat_id", "status", "user_id", "updated_at")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    chat_id: str
    status: MessageStatus
    user_id: str
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, message_id: _Optional[str] = ..., chat_id: _Optional[str] = ..., status: _Optional[_Union[MessageStatus, str]] = ..., user_id: _Optional[str] = ..., updated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
