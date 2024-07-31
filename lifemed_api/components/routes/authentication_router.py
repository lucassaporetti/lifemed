from fastapi import APIRouter, HTTPException
from lifemed_api.components.utils.jwt_utils import create_access_token
from datetime import timedelta

router = APIRouter()


@router.get(
    "/generate_token",
    summary="Generate a JWT token",
    description="Generate a JWT token for authentication using pre-configured settings"
)
async def generate_token():
    try:
        data = {
            "sub": "testuser"
        }
        token = create_access_token(data, expires_delta=timedelta(hours=1))
        return {"access_token": token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to generate token")
