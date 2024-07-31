run:
	uvicorn lifemed_api.components.api.api:app --reload &
	@echo "API is running at http://127.0.0.1:8000/swagger"
