from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from lifemed_api.components.schemas.monitoring_schema import Healthz
from lifemed_api.components.schemas.patient_schema import (
    PatientResponse,
    PatientRequest
)
from lifemed_api.components.business.patient_controller import PatientController
from lifemed_api.components.utils.authentication import JWTBearer
from lifemed_api.components.utils.parameter_validator import ParameterValidator

router = APIRouter()
validator = ParameterValidator()


@router.get("/", include_in_schema=False)
async def redirect_to_swagger():
    return RedirectResponse("/swagger")


@router.get("/healthz", response_model=Healthz, include_in_schema=False)
async def healthz():
    return Healthz()


@router.get(
    "/get_patient/{object_id}",
    response_model=PatientResponse,
    summary="Get patient data",
    description="Get patient data according to object_id parameter",
    dependencies=[Depends(JWTBearer())]
)
async def get_patient_data(request: Request, object_id: str):
    validator.validate(request, {})
    patient_controller = PatientController()
    return patient_controller.get_patient_data(patient_id=object_id)


@router.post(
    "/insert_patient",
    response_model=PatientResponse,
    summary="Insert a new patient",
    description="Insert a new patient with the given details",
    dependencies=[Depends(JWTBearer())]
)
async def insert_patient(request: Request, patient: PatientRequest):
    validator.validate(request, patient.dict())
    patient_controller = PatientController()
    return patient_controller.insert_patient(patient)


@router.put(
    "/update_patient/{object_id}",
    response_model=PatientResponse,
    summary="Update patient data",
    description="Update patient data for the given object_id",
    dependencies=[Depends(JWTBearer())]
)
async def update_patient(request: Request, object_id: str, patient: PatientRequest):
    validator.validate(request, patient.dict())
    patient_controller = PatientController()
    return patient_controller.update_patient(patient_id=object_id, patient_data=patient)


@router.delete(
    "/delete_patient/{object_id}",
    summary="Delete patient data",
    description="Delete patient data for the given object_id",
    dependencies=[Depends(JWTBearer())]
)
async def delete_patient(request: Request, object_id: str):
    validator.validate(request, {})
    patient_controller = PatientController()
    return patient_controller.delete_patient(patient_id=object_id)


def include_routes(app, logger):
    logger.info("loading routes")
    app.include_router(router)
