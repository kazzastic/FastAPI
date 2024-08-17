from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session 

from . import crud, models, schemas
from .database import SessionLocal, engine

import logging 
import sys

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/patients/", response_model = schemas.PatientResponseSchema)
def create_patient(patient: schemas.CreatePatient, db: Session = Depends(get_db)):

    db_user = crud.get_patient_by_email(db=db, email=patient.email)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")
    
    return crud.create_patient(db=db, patient=patient)

@app.get("/hello-world")
def hello_world():
    logger.debug('this is a debug message')
    return {"message": "hello world"}

@app.get("/patients/{id}", response_model = schemas.PatientResponseSchema)
def get_patient_by_id(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_patient_by_id(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user