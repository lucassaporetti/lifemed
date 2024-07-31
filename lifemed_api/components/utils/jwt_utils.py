import jwt
from datetime import datetime, timedelta

from lifemed_api.components.config import envs


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, envs.SECRET_KEY, algorithm=envs.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, envs.SECRET_KEY, algorithms=[envs.ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
