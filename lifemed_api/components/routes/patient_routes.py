from fastapi import APIRouter, Header
from fastapi.responses import RedirectResponse
import jwt

from lifemed_api.components.schemas.patient_schema import PatientData
from lifemed_api.components.business.patient_controller import PatientController
from lifemed_api.components.utils.authentication import authenticate

router = APIRouter()


@router.get("/", include_in_schema=False)
async def redirect_to_swagger():
    return RedirectResponse("/swagger")


@router.get(
    "/patients/{patient_id}",
    response_model=PatientData,
    summary="Get patient data",
    description="Get patient data according to patient_id parameter",
)
@authenticate
async def get_patient_data(patient_id: str, authorization: str = Header(default=None)):
    claims = jwt.decode(
        authorization.replace("Bearer ", ""), options={"verify_signature": True}
    )
    user_id = claims["user_id"]
    patient_controller = PatientController(user_id)
    return patient_controller.get_patient_data(patient_id=patient_id)


@router.post(
    "/patients",
    response_model=PatientData,
    summary="Create a new patient",
    description="Create a new patient with the given details",
)
async def create_patient(patient: PatientData, authorization: str = Header(default=None)):
    claims = jwt.decode(
        authorization.replace("Bearer ", ""), options={"verify_signature": True}
    )
    user_id = claims["user_id"]
    patient_controller = PatientController(user_id)
    return patient_controller.create_patient(patient)


@router.put(
    "/patients/{patient_id}",
    response_model=PatientData,
    summary="Update patient data",
    description="Update patient data for the given patient_id",
)
async def update_patient(patient_id: str, patient: PatientData, authorization: str = Header(default=None)):
    claims = jwt.decode(
        authorization.replace("Bearer ", ""), options={"verify_signature": True}
    )
    user_id = claims["user_id"]
    patient_controller = PatientController(user_id)
    return patient_controller.update_patient(patient_id, patient)


@router.delete(
    "/patients/{patient_id}",
    summary="Delete patient data",
    description="Delete patient data for the given patient_id",
)
async def delete_patient(patient_id: str, authorization: str = Header(default=None)):
    claims = jwt.decode(
        authorization.replace("Bearer ", ""), options={"verify_signature": True}
    )
    user_id = claims["user_id"]
    patient_controller = PatientController(user_id)
    return patient_controller.delete_patient(patient_id)


def include_routes(app, logger):
    logger.info("loading routes")
    app.include_router(router)
