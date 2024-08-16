from sqlalchemy.orm import Session
from . import models, schemas

def create_patient(db: Session, patient: schemas.CreatePatient):

    fake_hashed_password = patient.p_password + "notreallyhashed"
    patient_user = models.PatientInfo(
        id = 1,
        first_name = patient.first_name,
        last_name = patient.last_name,
        email = patient.email,
        p_personal_number = patient.p_personal_number,
        guardian_name = patient.guardian_name,
        address = patient.address,
        dob = patient.dob,
        visit_id = patient.visit_id,
        allergies = patient.allergies,
        medical_history = patient.medical_history,
        p_password = fake_hashed_password,
    )

    db.add(patient_user)
    db.commit()
    db.refresh(patient_user)

    return patient_user

def get_patient_by_email(db: Session, email: str):
    return db.query(models.PatientInfo).filter(models.PatientInfo.email == email).first()