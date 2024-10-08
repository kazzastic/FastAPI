from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, JSON
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

from .database import Base

# Setting up bcrypt context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PatientInfo(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key = True, nullable=False, autoincrement = True)
    first_name = Column(String, nullable = False)
    last_name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    p_personal_number = Column(String, nullable = False)
    guardian_name = Column(String, nullable = True)
    address = Column(String, nullable = False)
    dob = Column(Date, nullable = False)
    medical_history = Column(JSON, nullable = True)
    p_password = Column(String, nullable=False) 

    def set_password(self, raw_password: str):
        self.p_password = pwd_context.hash(raw_password)

    def verify_password(self, raw_password: str) -> bool:
        return pwd_context.verify(raw_password, self.p_password)