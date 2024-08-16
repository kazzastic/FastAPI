from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict
from datetime import date

class PatientSchema(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    p_personal_number: int = Field(..., gt = 0, description = "Should equal to 12")
    guardian_name: Optional[str] = Field(None, max_length = 50)
    address: str = Field(...)
    dob: date = Field(...)
    visit_id: int = Field(..., gt = 0, description = "Must be positive Int")
    allergies: Optional[List[str]] = Field(defualt = None)
    medical_history: Optional[Dict[str, str]] = Field(default = None)
    p_password: str = Field(..., min_length = 6, description = "Should be atleast 6 characters")

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Farwa",
                "last_name": "Naqvi",
                "email": "farwans6@gmail.com",
                "p_personal_number": "03410227736",
                "guardian_name": "Kazim Raza",
                "address": "Super chapal luxury apartment",
                "dob": "1999-11-19",
                "visit_id": "1",
                "allergies": ["something", "something_else"],
                "medical_history": {
                    "fever": "fucked up", 
                    "cough": "mild"
                },
                "p_password": "my_secure_password"
            }
        }

class CreatePatient(PatientSchema):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(...)
    p_personal_number: int = Field(..., gt = 0, description = "Should equal to 12")
    guardian_name: Optional[str] = Field(None, max_length = 50)
    address: str = Field(...)
    dob: date = Field(...)
    visit_id: int = Field(..., gt = 0, description = "Must be positive Int")
    allergies: Optional[List[str]] = Field(defualt = None)
    medical_history: Optional[Dict[str, str]] = Field(default = None)
    p_password: str = Field(..., min_length = 6, description = "Should be atleast 6 characters")

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Farwa",
                "last_name": "Naqvi",
                "email": "farwans6@gmail.com",
                "p_personal_number": "03410227736",
                "guardian_name": "Kazim Raza",
                "address": "Super chapal luxury apartment",
                "dob": "1999-11-19",
                "visit_id": "1",
                "allergies": ["something", "something_else"],
                "medical_history": {
                    "fever": "fucked up", 
                    "cough": "mild"
                },
                "p_password": "my_secure_password"
            }
        }

class PatientResponseSchema(PatientSchema):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    p_personal_number: int
    guardian_name: Optional[str]
    address: str
    dob: date
    visit_id: int
    allergies: Optional[List[str]]
    medical_history: Optional[Dict[str, str]]

    class Config:
        orm_mode = True