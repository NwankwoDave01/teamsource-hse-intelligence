# HSE Intelligence API (Backend)

The backend for HSE Intelligence, an AI-powered Health, Safety and Environment (HSE) Management and Incident Intelligence Platform for industrial businesses (oil and gas, manufacturing, construction, logistics and more).

Built with Python 3.13 and FastAPI.

Current status (Task 001): backend foundation with a health-check endpoint, Pydantic schemas, a service layer and automated tests. Database (PostgreSQL, SQLAlchemy, Alembic) and AI features come in later tasks.

## Prerequisites
Tool	Version	Check with
Git	any recent	git --version
Python	3.13	python3.13 --version
VS Code (or another IDE)	any	

Windows users: we recommend WSL (Ubuntu). Keep the project inside the Linux filesystem (e.g. ~/projects/), not under /mnt/c/.

## Setup

All commands below are run in a terminal.

### 1. Clone the repository
bash
git clone https://github.com/NwankwoDave01/teamsource-hse-intelligence.git
cd teamsource-hse-intelligence/backend
### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from everything else on your computer. Use one of the options below.

Option A: standard Python

bash
python3.13 -m venv .venv

Option B: using uv

bash
uv venv --python 3.13 .venv

### 3. Activate it
bash
source .venv/bin/activate          # Linux / WSL / macOS
# .venv\Scripts\activate           # Windows PowerShell

You should now see (.venv) at the start of your prompt. Confirm the version:

bash
python --version                   # should print Python 3.13.x

### 4. Install dependencies
bash
pip install -r requirements.txt
Run the application

From the backend/ folder, with the virtual environment active:

bash
uvicorn app.main:app --reload
app.main is the file app/main.py.
app after the colon is the FastAPI object inside that file.
--reload restarts the server automatically when you save a file (development only).

Once you see Application startup complete, open:

URL	What you get
http://127.0.0.1:8000/health	The health-check response (JSON)
http://127.0.0.1:8000/docs	Interactive API documentation (Swagger UI)
http://127.0.0.1:8000/redoc	Alternative API documentation

Stop the server with Ctrl + C.

### Example response
bash
curl http://127.0.0.1:8000/health
json
{
  "status": "ok",
  "service": "HSE Intelligence API",
  "version": "0.1.0"
}
Run the tests

From the backend/ folder, with the virtual environment active:

bash
python -m pytest

Useful variations:

bash
python -m pytest -v                          # verbose: one line per test
python -m pytest tests/test_health.py        # run a single file
python -m pytest -k "service"                # run tests whose name contains "service"

Use python -m pytest rather than plain pytest so Python can find the app package.

You may see a deprecation warning about httpx from the test client. It does not affect the results.

Project structure
teamsource-hse-intelligence/
├── README.md                     # Project overview
├── .gitignore
└── backend/
    ├── README.md                 # This file
    ├── requirements.txt          # Python dependencies
    ├── app/
    │   ├── main.py               # Creates the FastAPI app and registers routes
    │   ├── api/
    │   │   └── routes/
    │   │       └── health.py     # HTTP endpoints (thin: receive request, call service)
    │   ├── schemas/
    │   │   └── health.py         # Pydantic models: shape and validation of data
    │   └── services/
    │       └── health_service.py # Business logic (no HTTP knowledge)
    └── tests/                    # Automated tests (pytest)

### How a request flows through the code
Request → uvicorn → main.py → routes/health.py → services/health_service.py → schemas/health.py
Response ← JSON    ←          ←                 ←                           ←
Layer	Responsibility
Route	Receives the HTTP request and returns the response. Keeps no logic of its own.
Service	Holds the business logic. Can be tested without a web server.
Schema	Defines and validates the data going in and out of the API.
Team workflow (Git)

Never commit directly to main.

bash
git checkout main
git pull origin main                          # always start up to date
git checkout -b feature/short-description     # create your branch
# ...make changes...
git add .
git commit -m "Add health route tests"        # short, present tense
git push -u origin feature/short-description

Then open a Pull Request on GitHub and ask a teammate to review it before merging.

Branch names: feature/..., fix/..., docs/... Never commit: .venv/, __pycache__/, .env.

## Troubleshooting
Problem	Fix
ModuleNotFoundError: No module named 'app'	You are not in the backend/ folder. Run cd backend. Use python -m pytest.
command not found: uvicorn / pytest	The virtual environment is not active. Run source .venv/bin/activate.
Address already in use	Another server is on port 8000. Stop it, or run uvicorn app.main:app --reload --port 8001.
python3.13: command not found	Install Python 3.13 (e.g. uv python install 3.13, or the deadsnakes PPA on Ubuntu).
/favicon.ico 404 in the server log	Harmless. The browser is asking for a tab icon we don't have.
Roadmap
[x] Task 001: FastAPI foundation, health check, schemas, service layer, tests
[ ] PostgreSQL, SQLAlchemy models and Alembic migrations
[ ] Incident reporting endpoints
[ ] Authentication
[ ] React frontend integration
[ ] AI-powered incident analysis