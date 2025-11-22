import pika
import json
import logging
from typing import Callable, Dict, Any
from datetime import datetime

from shared.config import settings

class PresenceMessageBroker:
    def __init__(self):
        self.connection = None
        self.channel = None
        self._connect()
    
    def _connect(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.URLParameters(settings.RABBITMQ_URL)
            )
            self.channel = self.connection.channel()
            
            self.channel.exchange_declare(
                exchange='presence_events',
                exchange_type='topic',
                durable=True
            )
            
            logging.info("PresenceService connected to RabbitMQ")
        except Exception as e:
            logging.error(f"Failed to connect to RabbitMQ: {e}")
            self.connection = None
            self.channel = None
    
    def publish_presence_update(self, user_id: str, presence_data: Dict[str, Any]):
        if not self.channel:
            return
        
        try:
            message = {
                'user_id': user_id,
                'presence_data': presence_data,
                'timestamp': datetime.utcnow().isoformat()
            }
            
            self.channel.basic_publish(
                exchange='presence_events',
                routing_key=f'presence.update.{user_id}',
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type='application/json'
                )
            )
        except Exception as e:
            logging.error(f"Failed to publish presence update: {e}")
    
    def publish_typing_update(self, user_id: str, chat_id: str, is_typing: bool):
        if not self.channel:
            return
        
        try:
            message = {
                'user_id': user_id,
                'chat_id': chat_id,
                'is_typing': is_typing,
                'timestamp': datetime.utcnow().isoformat()
            }
            
            self.channel.basic_publish(
                exchange='presence_events',
                routing_key=f'typing.update.{chat_id}',
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=2,
                    content_type='application/json'
                )
            )
        except Exception as e:
            logging.error(f"Failed to publish typing update: {e}")

presence_broker = PresenceMessageBroker()