"""
Docstring for backend.models.org_member

Defines the model for the member's information within a specific department
"""
import uuid
from sqlalchemy import JSON, UUID, Column, ForeignKey
from sqlalchemy.orm import relationship
from backend.config.database import Base
import jsonschema

class DepartmentMember(Base):
    __tablename__ = "department_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    member_id = Column(UUID(as_uuid=True), ForeignKey("members.id"), nullable=False)
    department_id = Column(UUID(as_uuid=True), ForeignKey("departments.id"), nullable=False)
    additional_fields = Column(JSON, nullable=True)  # department-specific data

    member = relationship("Member", back_populates="department_memberships")
    department = relationship("Department", back_populates="department_members")

    def validate_additional_fields(self):
        """Validate additional_fields against the department's JSON schema."""
        if self.department and self.department.custom_fields and self.additional_fields:
            jsonschema.validate(instance=self.additional_fields, schema=self.department.custom_fields)
