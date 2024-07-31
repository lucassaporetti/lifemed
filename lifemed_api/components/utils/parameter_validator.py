from fastapi import Request, HTTPException


class ParameterValidator:
    def __init__(self):
        self.required_fields_map = {
            "POST": {
                "/patients": ["name", "birth_date", "phones", "plan_linked"]
            },
            "PUT": {
                "/patients/{object_id}": ["object_id", "name", "birth_date", "phones", "plan_linked"]
            },
            "GET": {
                "/patients/{object_id}": ["object_id"]
            },
            "DELETE": {
                "/patients/{object_id}": ["object_id"]
            },
        }

    def validate(self, request: Request, json_body: dict):
        path = request.url.path
        method = request.method

        required_fields = self.get_required_fields(path, method)

        if method == "POST":
            missing_fields = [field for field in required_fields if field not in json_body]
            if missing_fields:
                raise HTTPException(
                    status_code=422,
                    detail=f"Missing required fields: {', '.join(missing_fields)}"
                )
        elif method == "PUT":
            path_params = request.path_params
            if "object_id" not in path_params or not path_params["object_id"]:
                raise HTTPException(status_code=422, detail="Missing required path parameter: object_id")
            body_fields = set(json_body.keys())
            update_fields = set(required_fields) - {"object_id"}
            if not body_fields.intersection(update_fields):
                raise HTTPException(
                    status_code=422,
                    detail="At least one field must be present in the request body for update"
                )
        elif method in ["GET", "DELETE"]:
            path_params = request.path_params
            for param in required_fields:
                if param not in path_params or not path_params[param]:
                    raise HTTPException(status_code=422, detail=f"Missing required path parameter: {param}")

    def get_required_fields(self, path: str, method: str) -> list:
        for endpoint in self.required_fields_map.get(method, {}):
            if path.startswith(endpoint.split("{")[0]):
                return self.required_fields_map[method][endpoint]
        return []

    def add_route(self, method: str, path: str, required_fields: list):
        if method not in self.required_fields_map:
            self.required_fields_map[method] = {}
        self.required_fields_map[method][path] = required_fields
