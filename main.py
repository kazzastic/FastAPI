from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session 

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model = schemas.PatientSchema)
def create_patient(patient: schemas.CreatePatient, db: Session = Depends(get_db)):

    db_user = crud.get_patient_by_email(dv, email=patient.email)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")
    
    return crud.create_patient(db=db, patient=patient)
