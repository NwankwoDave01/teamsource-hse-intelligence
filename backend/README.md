# HSE Intelligence API (Backend)

The backend for **HSE Intelligence**, an AI-powered Health, Safety and Environment (HSE) Management and Incident Intelligence Platform for industrial businesses (oil and gas, manufacturing, construction, logistics and more).

Built with **Python 3.13** and **FastAPI**.

> **Current status (Task 001):** backend foundation with a health-check endpoint, Pydantic schemas, a service layer and automated tests. Database (PostgreSQL, SQLAlchemy, Alembic) and AI features come in later tasks.

---

## Prerequisites

| Tool | Version | Check with |
|---|---|---|
| Git | any recent | `git --version` |
| Python | 3.13 | `python3.13 --version` |
| VS Code (or another IDE) | any | |

Windows users: we recommend **WSL (Ubuntu)**. Keep the project inside the Linux filesystem (e.g. `~/projects/`), not under `/mnt/c/`.

---

## Setup

All commands below are run in a terminal.

### 1. Clone the repository and switch to `develop`

```bash
git clone https://github.com/NwankwoDave01/teamsource-hse-intelligence.git
cd teamsource-hse-intelligence
git checkout develop
cd backend
```

`develop` is our integration branch. Always start from it (see [Team workflow](#team-workflow-git)).

### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from everything else on your computer. Use **one** of the options below.

**Option A: standard Python**

```bash
python3.13 -m venv .venv
```

**Option B: using [uv](https://docs.astral.sh/uv/)**

```bash
uv venv --python 3.13 .venv
```

### 3. Activate it

```bash
source .venv/bin/activate          # Linux / WSL / macOS
# .venv\Scripts\activate           # Windows PowerShell
```

You should now see `(.venv)` at the start of your prompt. Confirm the version:

```bash
python --version                   # should print Python 3.13.x
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

`backend/requirements.txt` is the **single** dependency file for the backend. It lists the packages we use directly:

| Package | Purpose |
|---|---|
| `fastapi` | The web API framework |
| `uvicorn[standard]` | The server that runs the FastAPI app |
| `sqlalchemy` | Database access (used in later tasks) |
| `psycopg[binary]` | PostgreSQL driver (used in later tasks) |
| `alembic` | Database migrations (used in later tasks) |
| `pydantic-settings` | Configuration from environment variables (later tasks) |
| `pytest` | Test runner |
| `httpx` | Required by FastAPI's `TestClient` |

When you add a new dependency, add it to this file by hand and mention it in your pull request. Do **not** overwrite the file with `pip freeze`, because that captures every installed package, including unrelated ones.

---

## Run the application

From the `backend/` folder, with the virtual environment active:

```bash
uvicorn app.main:app --reload
```

- `app.main` is the file `app/main.py`.
- `app` after the colon is the FastAPI object inside that file.
- `--reload` restarts the server automatically when you save a file (development only).

Once you see `Application startup complete`, open:

| URL | What you get |
|---|---|
| http://127.0.0.1:8000/health | The health-check response (JSON) |
| http://127.0.0.1:8000/docs | Interactive API documentation (Swagger UI) |
| http://127.0.0.1:8000/redoc | Alternative API documentation |

Stop the server with `Ctrl + C`.

### Example response

```bash
curl http://127.0.0.1:8000/health
```

```json
{
  "status": "ok",
  "service": "HSE Intelligence API",
  "version": "0.1.0"
}
```

---

## Run the tests

From the `backend/` folder, with the virtual environment active:

```bash
python -m pytest
```

Useful variations:

```bash
python -m pytest -v                          # verbose: one line per test
python -m pytest tests/test_health.py        # run a single file
python -m pytest -k "health"                 # run tests whose name contains "health"
```

Use `python -m pytest` rather than plain `pytest` so Python can find the `app` package.

> You may see a deprecation warning about `httpx` from the test client. It does not affect the results.

---

## Project structure

```
teamsource-hse-intelligence/
├── README.md                     # Project overview
├── .gitignore
├── ai/                           # AI functionality (future tasks)
├── docs/                         # Project documentation
└── backend/
    ├── README.md                 # This file
    ├── requirements.txt          # The single backend dependency file
    ├── app/
    │   ├── main.py               # Creates the FastAPI app and registers routes
    │   ├── api/
    │   │   ├── routes/
    │   │   │   └── health.py     # HTTP endpoints (thin: receive request, call service)
    │   │   └── v1/               # Reserved for versioned API routes
    │   ├── core/                 # App configuration and settings (future)
    │   ├── db/                   # Database connection and sessions (future)
    │   ├── models/               # SQLAlchemy database models (future)
    │   ├── schemas/
    │   │   └── health.py         # Pydantic models: shape and validation of data
    │   └── services/
    │       └── health_service.py # Business logic (no HTTP knowledge)
    └── tests/
        └── test_health.py        # Automated tests (pytest)
```

Folders marked *(future)* currently contain only a `.gitkeep` placeholder so Git keeps the empty folder.

### How a request flows through the code

```
Request → uvicorn → main.py → routes/health.py → services/health_service.py → schemas/health.py
Response ← JSON    ←          ←                 ←                           ←
```

| Layer | Responsibility |
|---|---|
| **Route** | Receives the HTTP request and returns the response. Keeps no logic of its own. |
| **Service** | Holds the business logic. Can be tested without a web server. |
| **Schema** | Defines and validates the data going in and out of the API. |

---

## Team workflow (Git)

Our agreed workflow:

```
develop → feature branch → implementation → pull request to develop → code review → approval and merge
```

Rules:

- Never commit directly to `main` or `develop`.
- Create every feature branch from the **latest `develop`**.
- Open pull requests **targeting `develop`**.
- Do not force-push, and do not merge your own pull request.
- Do not delete files just to get rid of a merge conflict. Resolve it properly.

Start a new piece of work:

```bash
git fetch origin
git checkout develop
git pull origin develop                       # always start from the latest develop
git checkout -b feature/short-description     # create your branch
# ...make changes...
git add .
git commit -m "Add health route tests"        # short, present tense
git push -u origin feature/short-description
```

Then open a Pull Request on GitHub with **base branch: `develop`** and request a review.

While your branch is open and `develop` has moved on, bring in the latest changes:

```bash
git fetch origin
git checkout feature/short-description
git merge origin/develop
# resolve any conflicts, run the app and tests again, then:
git push
```

Branch names: `feature/...`, `fix/...`, `docs/...`

Never commit: `.venv/`, `__pycache__/`, `.env`, `*.bak`.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'app'` | You are not in the `backend/` folder. Run `cd backend`. Use `python -m pytest`. |
| `command not found: uvicorn` / `pytest` | The virtual environment is not active. Run `source .venv/bin/activate`. |
| `Address already in use` | Another server is on port 8000. Stop it, or run `uvicorn app.main:app --reload --port 8001`. |
| `python3.13: command not found` | Install Python 3.13 (e.g. `uv python install 3.13`, or the deadsnakes PPA on Ubuntu). |
| `git push` says the branch has no upstream | Run `git push -u origin <your-branch-name>` once. |
| Merge conflict after `git merge origin/develop` | Run `git status`, open each conflicted file, keep the correct content from both sides, then `git add` and `git commit`. To start over: `git merge --abort`. |
| `/favicon.ico 404` in the server log | Harmless. The browser is asking for a tab icon we don't have. |

---

## Roadmap

- [x] Task 001: FastAPI foundation, health check, schemas, service layer, tests
- [ ] PostgreSQL, SQLAlchemy models and Alembic migrations
- [ ] Incident reporting endpoints
- [ ] Authentication
- [ ] React frontend integration
- [ ] AI-powered incident analysis
