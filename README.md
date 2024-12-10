# Lifemed API

## Overview

This project is a RESTful API for management of medical clinics, developed using FastAPI. 
It includes database management with PostgreSQL, dependency management with Poetry, 
and containerization with Docker Compose. The following steps contain commands to be executed 
only in a Linux terminal. For Windows, I recommend using Git Bash.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.12.3**: [Download Python 3.12.3](https://www.python.org/downloads/release/python-3123/)
- **Poetry**: [Installation Guide](https://python-poetry.org/docs/#installation)
- **Docker**: [Docker Installation](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Docker Compose Installation](https://docs.docker.com/compose/install/)

## Setup

### 1. Clone the Repository

Start by cloning the repository to your local machine and then access the directory:

```sh
git clone https://github.com/lucassaporetti/lifemed.git
cd lifemed
```

### 2. Create and Activate a Virtual Environment

To ensure dependencies are managed correctly, create a Python virtual environment and activate it:

```sh
python3.9 -m venv venv
source venv/bin/activate
```

This isolates your Python environment from the global environment, preventing version conflicts.

### 3. Install Dependencies with Poetry

Use Poetry for dependency management. Install the required Python dependencies:

```sh
poetry install
```

### 4. Build and Start Docker Containers

Build and run the Docker containers with:

```sh
docker-compose up --build
```

This command builds the Docker images and starts the PostgreSQL container. 
It also ensures the database is initialized with lifemed_db schema.

### 5. Run the Application

To start the FastAPI application, leave docker running and open another terminal tab. 
Just use the makefile command on it:

```sh
make run
```

Or, if you want, use Uvicorn command. You can run it directly with:

```sh
uvicorn lifemed_api.components.api.api:app --reload
```

### 6. Accessing the Application

Once the application is running, you can access the API documentation at:

    Swagger UI: http://127.0.0.1:8000/swagger
    ReDoc: http://127.0.0.1:8000/docs

These URLs provide interactive documentation for testing and exploring the API.

### 7. Generate JWT token for authentication

To facilitate testing, you can generate a JWT token directly via the API. This token will be valid for 1 hour. 
Send a GET request to the `/generate_token` route:

```bash
curl -X GET "http://localhost:8000/generate_token
```

### OBS.: This application already has a Postman Collection included on main folder

## Troubleshooting:

Port Conflicts: Ensure that no other services are using the ports specified in 
the docker-compose.yml (e.g., port 5432 for PostgreSQL).

Docker Logs: If the database fails to initialize correctly, check Docker logs for errors.

## Contributing:

Feel free to contribute to the project by submitting issues or pull requests. 

This project is licensed under the MIT License. See the LICENSE file for details.
