from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
import uuid

from generated import auth_pb2
from .models import User, RefreshToken
from .security import (
    verify_password, 
    get_password_hash, 
    create_access_token, 
    create_refresh_token,
    verify_token,
    datetime_to_proto
)
from shared.config import settings
from shared.message_broker import message_broker, EventType

class AuthService:
    def __init__(self, db: Session):
        self.db = db

    def register(self, request: auth_pb2.RegisterRequest) -> auth_pb2.AuthResponse:
        existing_user = self.db.query(User).filter(
            (User.email == request.email) | (User.username == request.username)
        ).first()
        
        if existing_user:
            return auth_pb2.AuthResponse(
                success=False,
                message="User with this email or username already exists"
            )

        hashed_password = get_password_hash(request.password)
        user = User(
            email=request.email,
            username=request.username,
            first_name=request.first_name,
            last_name=request.last_name,
            hashed_password=hashed_password
        )
        
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except IntegrityError:
            self.db.rollback()
            return auth_pb2.AuthResponse(
                success=False,
                message="User creation failed"
            )

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})
        
        self._save_refresh_token(user.id, refresh_token)

        message_broker.publish(
            EventType.USER_REGISTERED,
            f"user.{user.id}.registered",
            {
                "user_id": str(user.id),
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return auth_pb2.AuthResponse(
            success=True,
            message="User registered successfully",
            access_token=access_token,
            refresh_token=refresh_token,
            user=self._user_to_proto(user),
            expires_at=datetime_to_proto(
                datetime.utcnow() + datetime.utcoffset(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
        )

    def login(self, request: auth_pb2.LoginRequest) -> auth_pb2.AuthResponse:
        user = self.db.query(User).filter(User.email == request.email).first()
        
        if not user or not verify_password(request.password, user.hashed_password):
            return auth_pb2.AuthResponse(
                success=False,
                message="Invalid email or password"
            )

        if not user.is_active:
            return auth_pb2.AuthResponse(
                success=False,
                message="Account is deactivated"
            )

        user.is_online = True
        user.last_seen = datetime.utcnow()
        self.db.commit()

        access_token = create_access_token({"sub": str(user.id)})
        refresh_token = create_refresh_token({"sub": str(user.id)})
        
        self._save_refresh_token(user.id, refresh_token)

        message_broker.publish(
            EventType.USER_LOGGED_IN,
            f"user.{user.id}.login",
            {
                "user_id": str(user.id),
                "email": user.email,
                "username": user.username,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return auth_pb2.AuthResponse(
            success=True,
            message="Login successful",
            access_token=access_token,
            refresh_token=refresh_token,
            user=self._user_to_proto(user),
            expires_at=datetime_to_proto(
                datetime.utcnow() + datetime.utcoffset(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
        )

    def refresh_token(self, request: auth_pb2.RefreshRequest) -> auth_pb2.AuthResponse:
        payload = verify_token(request.refresh_token)
        if not payload or payload.get("type") != "refresh":
            return auth_pb2.AuthResponse(
                success=False,
                message="Invalid refresh token"
            )

        user_id = payload.get("sub")
        user = self.db.query(User).filter(User.id == uuid.UUID(user_id)).first()
        
        if not user or not user.is_active:
            return auth_pb2.AuthResponse(
                success=False,
                message="User not found or inactive"
            )

        token_record = self.db.query(RefreshToken).filter(
            RefreshToken.token == request.refresh_token,
            RefreshToken.is_revoked == False
        ).first()
        
        if not token_record:
            return auth_pb2.AuthResponse(
                success=False,
                message="Token revoked"
            )

        new_access_token = create_access_token({"sub": str(user.id)})
        new_refresh_token = create_refresh_token({"sub": str(user.id)})
        
        token_record.is_revoked = True
        self._save_refresh_token(user.id, new_refresh_token)
        self.db.commit()

        return auth_pb2.AuthResponse(
            success=True,
            message="Token refreshed successfully",
            access_token=new_access_token,
            refresh_token=new_refresh_token,
            user=self._user_to_proto(user),
            expires_at=datetime_to_proto(
                datetime.utcnow() + datetime.utcoffset(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            )
        )

    def validate_token(self, request: auth_pb2.ValidateRequest) -> auth_pb2.ValidateResponse:
        payload = verify_token(request.access_token)
        if not payload or payload.get("type") != "access":
            return auth_pb2.ValidateResponse(is_valid=False, error="Invalid token")

        user_id = payload.get("sub")
        user = self.db.query(User).filter(User.id == uuid.UUID(user_id)).first()
        
        if not user or not user.is_active:
            return auth_pb2.ValidateResponse(is_valid=False, error="User not found")

        return auth_pb2.ValidateResponse(is_valid=True, user_id=str(user.id))

    def logout(self, request: auth_pb2.LogoutRequest) -> auth_pb2.LogoutResponse:
        if request.refresh_token:
            token_record = self.db.query(RefreshToken).filter(
                RefreshToken.token == request.refresh_token
            ).first()
            if token_record:
                token_record.is_revoked = True

        user = self.db.query(User).filter(User.id == uuid.UUID(request.user_id)).first()
        if user:
            user.is_online = False
            user.last_seen = datetime.utcnow()

        self.db.commit()

        message_broker.publish(
            EventType.USER_LOGGED_OUT,
            f"user.{request.user_id}.logout",
            {
                "user_id": request.user_id,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return auth_pb2.LogoutResponse(success=True)

    def update_profile(self, request: auth_pb2.UpdateProfileRequest) -> auth_pb2.ProfileResponse:
        user = self.db.query(User).filter(User.id == uuid.UUID(request.user_id)).first()
        if not user:
            return auth_pb2.ProfileResponse()

        if request.username:
            user.username = request.username
        if request.first_name:
            user.first_name = request.first_name
        if request.last_name:
            user.last_name = request.last_name
        if request.avatar_url:
            user.avatar_url = request.avatar_url

        user.updated_at = datetime.utcnow()
        self.db.commit()
        self.db.refresh(user)

        message_broker.publish(
            EventType.USER_PROFILE_UPDATED,
            f"user.{request.user_id}.profile_updated",
            {
                "user_id": request.user_id,
                "username": request.username,
                "first_name": request.first_name,
                "last_name": request.last_name,
                "avatar_url": request.avatar_url,
                "timestamp": datetime.utcnow().isoformat()
            }
        )

        return auth_pb2.ProfileResponse(user=self._user_to_proto(user))

    def _save_refresh_token(self, user_id: uuid.UUID, token: str):
        expires_at = datetime.utcnow() + datetime.utcoffset(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = RefreshToken(
            user_id=user_id,
            token=token,
            expires_at=expires_at
        )
        self.db.add(refresh_token)
        self.db.commit()

    def _user_to_proto(self, user: User) -> auth_pb2.User:
        return auth_pb2.User(
            id=str(user.id),
            email=user.email,
            username=user.username,
            first_name=user.first_name or "",
            last_name=user.last_name or "",
            avatar_url=user.avatar_url or "",
            is_online=user.is_online,
            last_seen=datetime_to_proto(user.last_seen),
            created_at=datetime_to_proto(user.created_at),
            updated_at=datetime_to_proto(user.updated_at)
        )