import grpc
from concurrent import futures
import logging
import signal
import sys

from generated import presence_pb2_grpc
from shared.config import settings
from .service import PresenceService

class PresenceServicer(presence_pb2_grpc.PresenceServiceServicer):
    def __init__(self):
        self.presence_service = PresenceService()
    
    def UpdatePresence(self, request, context):
        return self.presence_service.update_presence(request)
    
    def GetOnlineUsers(self, request, context):
        return self.presence_service.get_online_users(request)
    
    def StreamPresenceUpdate(self, request, context):
        # TODO: Implement streaming
        pass
    
    def UpdateTypingStatus(self, request, context):
        return self.presence_service.update_typing_status(request)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    presence_pb2_grpc.add_PresenceServiceServicer_to_server(PresenceServicer(), server)
    server.add_insecure_port(f'[::]:{settings.PRESENCE_SERVICE_PORT}')
    
    def graceful_shutdown(signum, frame):
        logging.info("Received shutdown signal")
        server.stop(5)
        sys.exit(0)
    
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    
    logging.info(f"Starting PresenceService on port {settings.PRESENCE_SERVICE_PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    serve()