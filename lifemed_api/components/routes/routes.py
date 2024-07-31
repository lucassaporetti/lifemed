from fastapi import APIRouter

from lifemed_api.components.routes import patient_routes


router = APIRouter()


def include_routers(app):
    app.include_router(patient_routes.router, prefix="/patients", tags=["patients"])


include_routers(router)
