from functools import wraps
from fastapi import Header, HTTPException
import jwt
from datetime import datetime, timedelta

from lifemed_api.components.config import envs


def verify_token(token: str) -> bool:
    try:
        payload = jwt.decode(token, envs.SECRET_KEY, algorithms=["HS256"])

        # if datetime.utcnow() > datetime.fromtimestamp(payload["exp"]):
        #     return False

        if "user_id" not in payload:
            return False

        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False


def authenticate(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        authorization = kwargs.get("authorization", None)
        if not authorization or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Unauthorized: Missing or invalid token")
        token = authorization.replace("Bearer ", "")
        if not verify_token(token):
            raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")
        return await func(*args, **kwargs)

    return wrapper
