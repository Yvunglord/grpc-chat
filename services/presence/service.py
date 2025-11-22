import json
from datetime import datetime, timedelta
from typing import List, Dict, Any
import logging

from google.protobuf.timestamp_pb2 import Timestamp

from shared.redis_client import redis_client
from generated import presence_pb2
from .models import PresenceState, UserStatus
from .message_broker import presence_broker
from shared.message_broker import message_broker, EventType

class PresenceService:
    def __init__(self):
        self.redis = redis_client.get_client()
        self.presence_key_prefix = 'presence:'
        self.online_users_key = 'online_users'
        self.typing_code_prefix = 'typing:'

    def _datetime_to_proto(self, dt: datetime) -> Timestamp:
        proto_timestamp = Timestamp()
        proto_timestamp.FromDatetime(dt)
        return proto_timestamp
    
    def _get_presence_key(self, user_id: str) -> str:
        return f"{self.presence_key_prefix}{user_id}"
    
    def _get_typing_key(self, chat_id: str, user_id: str) -> str:
        return f"{self.typing_code_prefix}{chat_id}:{user_id}"
    
    def update_presence(self, request: presence_pb2.PresenceUpdate) -> presence_pb2.PresenceResponse:
        try:
            user_id = request.user_id
            status = UserStatus(request.status)
            custom_status = request.custom_status
            is_typing = request.is_typing
            chat_id = request.chat_id

            presence_data = {
                "user_id": user_id,
                "status": status.value,
                "custom_status": custom_status or "",
                "last_seen": datetime.utcnow().isoformat(),
                "is_typing": str(is_typing),
                "chat_id": chat_id or ""
            }

            key = self._get_presence_key(user_id)
            self.redis.hset(key, mapping=presence_data)
            self.redis.expire(key, timedelta(minutes=5))

            if status == UserStatus.ONLINE:
                self.redis.sadd(self.online_users_key, user_id)
            else:
                self.redis.srem(self.online_users_key, user_id)

            presence_broker.publish_presence_update(user_id, presence_data)

            return presence_pb2.PresenceResponse(
                success=True,
                message="Presence updated successfully",
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )
        
        except Exception as e:
            logging.error(f"Error updating presence: {e}")
            return presence_pb2.PresenceResponse(
                success=False,
                message=str(e),
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )
        
    def get_online_users(self, request: presence_pb2.OnlineUsersRequest) -> presence_pb2.OnlineUsersResponse:
        try:
            chat_id = request.chat_id
            user_ids = list(request.user_ids)
            limit = request.limit
            
            online_user_ids = self.redis.smembers(self.online_users_key)
            
            if user_ids:
                online_user_ids = [uid for uid in online_user_ids if uid in user_ids]
            
            if limit > 0:
                online_user_ids = list(online_user_ids)[:limit]
            
            online_users = []
            for user_id in online_user_ids:
                key = self._get_presence_key(user_id)
                data = self.redis.hgetall(key)
                
                if data:
                    presence_update = presence_pb2.PresenceUpdate(
                        user_id=user_id,
                        status=int(data.get("status", 0)),
                        custom_status=data.get("custom_status", ""),
                        is_typing=bool(data.get("is_typing", "False")),
                        chat_id=data.get("chat_id", "")
                    )
                    
                    last_seen_str = data.get("last_seen")
                    if last_seen_str:
                        last_seen = datetime.fromisoformat(last_seen_str)
                        presence_update.last_seen.CopyFrom(self._datetime_to_proto(last_seen))
                    
                    online_users.append(presence_update)
            
            return presence_pb2.OnlineUsersResponse(
                online_users=online_users,
                total_count=len(online_users),
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )
            
        except Exception as e:
            logging.error(f"Error getting online users: {e}")
            return presence_pb2.OnlineUsersResponse(
                online_users=[],
                total_count=0,
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )
        
    def update_typing_status(self, request: presence_pb2.TypingUpdate) -> presence_pb2.PresenceResponse:
        try:
            user_id = request.user_id
            chat_id = request.chat_id
            is_typing = request.is_typing
            
            typing_key = self._get_typing_key(chat_id, user_id)
            if is_typing:
                self.redis.set(typing_key, "1", ex=10)
            else:
                self.redis.delete(typing_key)
            
            presence_key = self._get_presence_key(user_id)
            if self.redis.exists(presence_key):
                self.redis.hset(presence_key, "is_typing", str(is_typing))
                if chat_id:
                    self.redis.hset(presence_key, "chat_id", chat_id)
            
            presence_broker.publish_typing_update(user_id, chat_id, is_typing)
            
            return presence_pb2.PresenceResponse(
                success=True,
                message="Typing status updated",
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )
            
        except Exception as e:
            logging.error(f"Error updating typing status: {e}")
            return presence_pb2.PresenceResponse(
                success=False,
                message=str(e),
                timestamp=self._datetime_to_proto(datetime.utcnow())
            )