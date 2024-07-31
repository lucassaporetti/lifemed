from fastapi import HTTPException
import uuid

from lifemed_api.components.schemas.patient_schema import PatientData
from lifemed_api.components.utils.database.service import DatabaseService
from lifemed_api.components.models.patient_model import Patient


class PatientController:
    def __init__(self, user_id: str):
        self.user_id = user_id

    def get_patient_data(self, patient_id: str):
        with DatabaseService() as db:
            patient = db.query(Patient).filter(Patient.uuid == patient_id).first()
            if not patient:
                raise HTTPException(status_code=404, detail="Patient not found")
            return PatientData.from_orm(patient)

    def create_patient(self, patient_data: PatientData):
        with DatabaseService() as db:
            new_uuid = str(uuid.uuid4())
            patient = Patient(
                uuid=new_uuid,
                name=patient_data.name,
                birth_date=patient_data.birth_date,
                phones=patient_data.phones,
                plan_linked=patient_data.plan_linked
            )
            db.add(patient)
            db.commit()
            return PatientData.from_orm(patient)

    def update_patient(self, patient_id: str, patient_data: PatientData):
        with DatabaseService() as db:
            patient = db.query(Patient).filter(Patient.uuid == patient_id).first()
            if not patient:
                raise HTTPException(status_code=404, detail="Patient not found")
            patient.name = patient_data.name
            patient.birth_date = patient_data.birth_date
            patient.phones = patient_data.phones
            patient.plan_linked = patient_data.plan_linked
            db.commit()
            return PatientData.from_orm(patient)

    def delete_patient(self, patient_id: str):
        with DatabaseService() as db:
            patient = db.query(Patient).filter(Patient.uuid == patient_id).first()
            if not patient:
                raise HTTPException(status_code=404, detail="Patient not found")
            db.remove(patient)
            db.commit()
            return {"message": "Patient deleted successfully"}
