"""
Docstring for backend.models.member_class

Model defines the information about member to a specific class and 
their attendance in the class
"""
import uuid
from sqlalchemy import JSON, UUID, Column, DateTime, Enum, ForeignKey, Text, func
from sqlalchemy.orm import relationship
from backend.config.database import Base

class MemberClass(Base):
    __tablename__ = "member_classes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    member_id = Column(UUID(as_uuid=True), ForeignKey("members.id"), nullable=False)
    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"), nullable=False)
    enrolled_at = Column(DateTime(timezone=True), server_default=func.now())
    attendance = Column(JSON, nullable=True)  # date mapped to status: present, absent, excused, tardy

    member = relationship("Member", back_populates="member_classes")
    class_ = relationship("Class", back_populates="member_classes")