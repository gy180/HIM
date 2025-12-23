import enum
import uuid
from sqlalchemy import JSON, UUID, Column, DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import relationship
from backend.config.database import Base

class Department(Base):
    __tablename__ = "departments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    custom_fields = Column(JSON, nullable=True)  # JSON Schema for department-specific fields

    # Relationships
    department_members = relationship("DepartmentMember", back_populates="department")
    classes = relationship("Class", back_populates="department")
