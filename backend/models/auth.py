"""
Docstring for backend.models.auth

For third party authentication
"""
import enum
import uuid
from sqlalchemy import UUID, Column, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class ProviderEnum(enum.Enum):
    google = "google"
    facebook = "facebook"
    apple = "apple"
    
class AuthIdentity(Base):
    __tablename__ = "auth_identities"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("members.id"), nullable=False)
    provider = Column(Enum(ProviderEnum), nullable=False)
    provider_id = Column(Text, nullable=False)

    user = relationship("Member", back_populates="auth_identities")