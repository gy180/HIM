"""
Docstring for backend.models.class

classes table for the classes within the department
"""
import uuid
from sqlalchemy import UUID, Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Class(Base):
    __tablename__ = "classes"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    room_id = Column(UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=True)
    teacher_id = Column(UUID(as_uuid=True), ForeignKey("members.id"), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    cost = Column(Integer, default=0)
    max_capacity = Column(Integer, nullable=True)

    department = relationship("Department", back_populates="classes")
    room = relationship("Room")
    teacher = relationship("Member")
    member_classes = relationship("MemberClass", back_populates="class_")