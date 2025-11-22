import grpc
from concurrent import futures
import logging
import signal
import sys

from generated import auth_pb2_grpc
from shared.database import init_db
from shared.config import settings
from .service import AuthService

class AuthServicer(auth_pb2_grpc.AuthServiceServicer):
    def Register(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.register(request)

    def Login(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.login(request)

    def RefreshToken(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.refresh_token(request)

    def ValidateToken(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.validate_token(request)

    def Logout(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.logout(request)

    def UpdateProfile(self, request, context):
        from shared.database import get_db
        with get_db() as db:
            service = AuthService(db)
            return service.update_profile(request)

def serve():
    init_db()
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_AuthServiceServicer_to_server(AuthServicer(), server)
    server.add_insecure_port(f'[::]:{settings.AUTH_SERVICE_PORT}')
    
    def graceful_shutdown(signum, frame):
        logging.info("Received shutdown signal")
        server.stop(5)
        sys.exit(0)
    
    signal.signal(signal.SIGINT, graceful_shutdown)
    signal.signal(signal.SIGTERM, graceful_shutdown)
    
    logging.info(f"Starting AuthService on port {settings.AUTH_SERVICE_PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    serve()