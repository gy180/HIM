import enum
import uuid
from sqlalchemy import UUID, Column, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    capacity = Column(Integer, nullable=True)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)