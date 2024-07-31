from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import json


class ValidateParamsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        method = request.method
        body = {}

        try:
            body = await request.json()
        except json.JSONDecodeError:
            pass

        if method in ["POST", "PUT"]:
            required_fields = self.get_required_fields(path, method)

            missing_fields = [field for field in required_fields if field not in body]
            if missing_fields:
                raise HTTPException(
                    status_code=422,
                    detail=f"Missing required fields: {', '.join(missing_fields)}"
                )

        path_params = request.path_params
        if "patient_id" in path_params:
            if not path_params["patient_id"]:
                raise HTTPException(status_code=422, detail="Missing required path parameter: patient_id")

        response = await call_next(request)
        return response

    def get_required_fields(self, path: str, method: str) -> list:

        required_fields_map = {
            "/patients": {
                "POST": ["name", "birth_date", "plan_linked"],
                "PUT": ["name", "birth_date", "plan_linked"]
            },
            "/patients/{patient_id}": {
                "GET": ["patient_id"],
                "PUT": ["patient_id", "name", "birth_date", "plan_linked"],
                "DELETE": ["patient_id"]
            },
        }

        base_path = path.split('{')[0]
        return required_fields_map.get(base_path, {}).get(method, [])
