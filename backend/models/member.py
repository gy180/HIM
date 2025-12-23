"""
Docstring for backend.models.member

Model for the member schema within the database
"""
import enum
import uuid
from sqlalchemy import JSON, UUID, Column, Date, DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import relationship
from backend.config.database import Base


class RoleEnum(enum.Enum):
    student = "student"
    teacher = "teacher"
    leader = "leader"
    assistant = "assistant"
    member = "member"
    guest = "guest"


class Member(Base):
    __tablename__ = "members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = Column(String(255), nullable=False)
    birthday = Column(Date, nullable=True)
    personal_phone = Column(String(20), nullable=True)
    work_phone = Column(String(20), nullable=True)
    mobile_phone = Column(String(20), nullable=True)
    address = Column(String(500), nullable=True)
    email = Column(String(255), unique=True, nullable=False)
    ssn = Column(String(20), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    role = Column(Enum(RoleEnum), nullable=False)
    line_id = Column(String(255), nullable=True)
    photo = Column(String(500), nullable=True)
    
    # JSON/ARRAY fields
    parents = Column(JSON, nullable=True)  # list of dict {member_id, name}
    family_members = Column(JSON, nullable=True)  # list of dict {member_id, name}
    additional_fields = Column(JSON, nullable=True)

    # Relationships
    department_memberships = relationship("DepartmentMember", back_populates="member")
    auth_identities = relationship("AuthIdentity", back_populates="member")
    member_classes = relationship("MemberClass", back_populates="member")

    @property
    def departments(self):
        """Return list of departments this member belongs to."""
        return [dm.department for dm in self.department_memberships]