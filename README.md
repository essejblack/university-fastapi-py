# FastAPI Sample Project

This repo is a Python-based project designed to provide a flexible and efficient API framework.
It is sample of University Endpoints. It contains tests , routes , migrations , schemas , ... 

## Features

- Modular and extensible architecture
- Easy integration with existing Python projects
- Clear and concise API endpoints

## Libraries
- alembic
- sqlalchemy
- pydantic-settings
- dotenv
- unit test (mock)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/FAPI.git
   cd FAPI
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Docker

You can also build and run the project using Docker:

1. Build it:
   ```bash
   docker compose build --no-cache
   ```

2. Run the Docker container:
   ```bash
   docker compose up -d
   ```

3. The API will be available at `http://localhost:8080`.

4. Access the API endpoints as described in the documentation.

## Configuration

- Edit the `config.py` file to adjust settings as needed.