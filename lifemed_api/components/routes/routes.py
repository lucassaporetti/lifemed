from fastapi import APIRouter

from lifemed_api.components.routes import (
    patient_routes,
    authentication_router
)


router = APIRouter()


def include_routers(app):
    app.include_router(patient_routes.router, prefix="/patients", tags=["patients"])
    app.include_router(authentication_router.router, prefix="/authentication", tags=["authentication"])


include_routers(router)
