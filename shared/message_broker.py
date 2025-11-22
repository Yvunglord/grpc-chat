import pika
import json
import logging
import threading
from typing import Dict, Callable, Any, List
from enum import Enum
from datetime import datetime

from .config import settings

class EventType(Enum):
    USER_REGISTERED = "user.registered"
    USER_LOGGED_IN = "user.logged_in"
    USER_LOGGED_OUT = "user.logged_out"
    USER_PROFILE_UPDATED = "user.profile_updated"

    PRESENCE_UPDATED = "presence.updated"
    TYPING_STATUS_UPDATED = "typing.status_updated"
    USER_WENT_ONLINE = "user.went_online"
    USER_WENT_OFFLINE = "user.went_offline"

    CHAT_CREATED = "chat.created"
    CHAT_UPDATED = "chat.updated"
    MESSAGE_SENT = "message.sent"
    MESSAGE_EDITED = "message.edited"
    MESSAGE_DELETED = "message.deleted"
    USER_JOINED_CHAT = "user.joined_chat"
    USER_LEFT_CHAT = "user.left_chat"

    NOTIFICATION_CREATED = "notification.created"
    NOTIFICATION_READ = "notification.read"

class MessageBroker:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(MessageBroker, cls).__new__(cls)
                cls._instance._initialized() = False
            return cls._instance
        
    def __init__(self):
        if self._initialized():
            return
        self.connection = None
        self.channel = None
        self.consumers = {}
        self._connect()
        self._initialized = True

    def _connect(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.URLParameters(settings.RABBITMQ_URL)
            )
            self.channel = self.connection.channel()

            self.channel.exchange_declare(
                exchange='chat_events',
                exchange_type='topic',
                durable=True
            )

            logging.info("Connected to RabbitMQ")
        except Exception as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")
            raise

    def publish(self, event_type: EventType, routing_key: str, data: Dict[str, Any]):
        if not self.channel:
            logging.error("No RabbitMQ connection")
            return
        
        try:
            message = {
                'event_type': event_type.value,
                'routing_key': routing_key,
                'data': data,
                'timestamp': datetime.utcnow().isoformat()
            }
            
            self.channel.basic_publish(
                exchange='chat_events',
                routing_key=routing_key,
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type='application/json',
                    type=event_type.value
                )
            )
            logging.debug(f"Published event: {event_type.value} -> {routing_key}")
        except Exception as e:
            logging.error(f"Failed to publish event: {e}")

    def subscribe(self, queue_name: str, routing_keys: List[str], callback: Callable):
        if not self.channel:
            logging.error("No RabbitMQ connection")
            return
        
        try:
            self.channel.queue_declare(queue=queue_name, durable=True)
            for routing_key in routing_keys:
                self.channel.queue_bind(
                    exchange='chat_events',
                    queue=queue_name,
                    routing_key=routing_key
                )

            self.channel.basic_consume(
                queue=queue_name,
                on_message_callback=callback,
                auto_ack=False
            )

            logging.info(f"Subscribed to {routing_keys} on queue {queue_name}")
        except Exception as e:
            logging.error(f"Failed to subscribe: {e}")

    def start_consuming(self):
        if self.channel:
            logging.info("Starting to consume messages...")
            self.channel.start_consuming()

    def close(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            logging.info("RabbitMQ connection closed")

message_broker = MessageBroker()