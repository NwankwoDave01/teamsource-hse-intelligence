# HSE Intelligence API (Backend)

The backend for **HSE Intelligence**, an AI-powered Health, Safety and Environment (HSE) Management and Incident Intelligence Platform for industrial businesses (oil and gas, manufacturing, construction, logistics and more).

Built with **Python 3.13**, **FastAPI**, **PostgreSQL**, **SQLAlchemy** and **Alembic**.

> **Current status**
> - Task 001: FastAPI foundation, health check, schemas, service layer, tests
> - Task 002: PostgreSQL integration, environment-based configuration, Alembic migrations, and the initial Organisation, Site and User models

---

## Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Database setup](#database-setup)
4. [Run the application](#run-the-application)
5. [Run the tests](#run-the-tests)
6. [Database migrations (Alembic)](#database-migrations-alembic)
7. [Project structure](#project-structure)
8. [Team workflow (Git)](#team-workflow-git)
9. [Troubleshooting](#troubleshooting)
10. [Roadmap](#roadmap)

---

## Prerequisites

| Tool | Version | Check with |
|---|---|---|
| Git | any recent | `git --version` |
| Python | 3.13 | `python3.13 --version` |
| PostgreSQL | 14 or newer | `psql --version` |
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

You should now see `(.venv)` at the start of your prompt. Confirm the version and location:

```bash
python --version                   # should print Python 3.13.x
which python                       # should end in backend/.venv/bin/python
```

The virtual environment must be active every time you work on the backend. The `.venv` folder is never committed, so every developer creates their own.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

`backend/requirements.txt` is the **single** dependency file for the backend:

| Package | Purpose |
|---|---|
| `fastapi` | The web API framework |
| `uvicorn[standard]` | The server that runs the FastAPI app |
| `sqlalchemy` | Database access (ORM) |
| `psycopg[binary]` | PostgreSQL driver |
| `alembic` | Database migrations |
| `pydantic-settings` | Configuration from environment variables |
| `pytest` | Test runner |
| `httpx` | Required by FastAPI's `TestClient` |

When you add a dependency, add it to this file by hand and mention it in your pull request. Do **not** overwrite the file with `pip freeze`, because that captures every installed package, including unrelated ones.

---

## Database setup

Each developer runs their **own local PostgreSQL**. Git shares the database *structure* (through migrations), never the data or passwords.

### 1. Install and start PostgreSQL (Ubuntu / WSL)

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo service postgresql start          # on systemd setups: sudo systemctl start postgresql
```

### 2. Create your database user and two databases

We use two databases: one for development and one for automated tests, so tests never touch your development data.

```bash
sudo -u postgres psql -c "CREATE USER hse_user WITH PASSWORD 'choose_a_simple_password';"
sudo -u postgres psql -c "CREATE DATABASE hse_intelligence OWNER hse_user;"
sudo -u postgres psql -c "CREATE DATABASE hse_intelligence_test OWNER hse_user;"
```

Choose your own password. Use only letters and digits while developing. Special characters (`@ : / # %`) have a meaning inside a URL and must be percent-encoded, which is a common source of errors.

### 3. Create your `.env` file

```bash
cp .env.example .env
```

Open `.env` and replace `change_me` with your password, in **both** lines:

```
DATABASE_URL=postgresql+psycopg://hse_user:change_me@localhost:5432/hse_intelligence
TEST_DATABASE_URL=postgresql+psycopg://hse_user:change_me@localhost:5432/hse_intelligence_test
```

| Variable | Used for |
|---|---|
| `DATABASE_URL` | The running application and development migrations |
| `TEST_DATABASE_URL` | Automated tests. **It must always point at the `_test` database.** |

Rules:

- `.env` is listed in `.gitignore`. **Never commit it**, and never paste passwords into chats, issues or pull requests.
- `.env.example` is committed and contains fake values only. If you add a new variable, add it there too.
- Check that your file is ignored: `git check-ignore -v .env` should print a matching rule.

### 4. Check the connection

Test the login on its own, before involving Python:

```bash
psql "postgresql://hse_user:your_password@127.0.0.1:5432/hse_intelligence" -c "SELECT 1;"
```

You should see a table containing `1`.

### 5. Create the tables

```bash
python -m alembic upgrade head
```

Confirm they exist:

```bash
psql "postgresql://hse_user:your_password@127.0.0.1:5432/hse_intelligence" -c "\dt"
```

You should see `organisations`, `sites`, `users` and `alembic_version`.

### Data model

```
Organisation ──< Site
     │            │
     └───────< User >──(optional)── Site
```

| Table | Key columns | Notes |
|---|---|---|
| `organisations` | `id` (UUID), `name` (unique), `is_active` | A customer company. The top of the multi-tenant hierarchy. |
| `sites` | `id`, `organisation_id`, `name`, `location` | Name is unique **within** an organisation. |
| `users` | `id`, `organisation_id`, `site_id` (optional), `email` (unique), `full_name`, `role`, `is_active` | Every user belongs to one organisation. |

Design decisions:

- **UUID primary keys**, so record IDs cannot be guessed across organisations.
- **Multi-tenancy:** every site and user row carries a required `organisation_id`. All future tables (e.g. incidents) must do the same.
- **`ondelete="RESTRICT"`** on organisation references: an organisation that still has sites or users cannot be deleted by accident.
- All tables have `created_at` and `updated_at` timestamps.

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
python -m pytest -v
```

Useful variations:

```bash
python -m pytest tests/test_health.py        # run a single file
python -m pytest tests/test_database.py      # database tests only
python -m pytest -k "relationships"          # tests whose name contains "relationships"
```

Use `python -m pytest` rather than plain `pytest` so Python can find the `app` package.

How the database tests work:

- They run the **real Alembic migrations** against `TEST_DATABASE_URL`, so they also verify the migrations.
- Each test runs inside a transaction that is **rolled back** afterwards, so tests don't leave data behind or affect each other.
- At the end of the run, the test database is migrated back down (`downgrade base`). **`TEST_DATABASE_URL` must therefore never point at a database you care about.**
- If `TEST_DATABASE_URL` is not set, the database tests are *skipped*, not failed. Check the summary line for `skipped`.

> You may see a deprecation warning about `httpx` from the test client. It does not affect the results.

---

## Database migrations (Alembic)

A **migration** is a versioned script that changes the database structure. Migrations live in `alembic/versions/` and are committed to Git, so the whole team shares the same database history.

Always run Alembic as `python -m alembic ...` from the `backend/` folder, so the copy inside your virtual environment is used.

| Task | Command |
|---|---|
| Apply all pending migrations | `python -m alembic upgrade head` |
| Show the current database version | `python -m alembic current` |
| Show migration history | `python -m alembic history` |
| Undo the last migration | `python -m alembic downgrade -1` |
| Undo everything | `python -m alembic downgrade base` |
| Check for a single latest version | `python -m alembic heads` (must list exactly one) |

### Changing a model

1. Edit the model in `app/models/`. A new model must also be imported in `app/models/__init__.py`.
2. Generate a migration:
   ```bash
   python -m alembic revision --autogenerate -m "short description of the change"
   ```
3. **Open the generated file in `alembic/versions/` and read it.** Autogenerate is a draft. Check `upgrade()` and `downgrade()`.
4. Apply it: `python -m alembic upgrade head`
5. Test the way back: `python -m alembic downgrade -1`, then `python -m alembic upgrade head`.
6. Run the tests and commit the model change **together with** its migration file.

### Migration rules for the team

- **One person creates migrations per branch.** Two people generating migrations from the same starting point creates two "heads" and a conflict that is painful to fix.
- **Never edit a migration that has already been merged.** Create a new one.
- After pulling someone else's migration, run `python -m alembic upgrade head` to bring your own database up to date.

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
    ├── .env.example              # Template for environment variables (fake values)
    ├── .env                      # YOUR local settings (git-ignored, never committed)
    ├── alembic.ini               # Alembic settings
    ├── alembic/
    │   ├── env.py                # Connects Alembic to our models and DATABASE_URL
    │   └── versions/             # Migration scripts (committed)
    ├── app/
    │   ├── main.py               # Creates the FastAPI app and registers routes
    │   ├── api/
    │   │   ├── routes/
    │   │   │   └── health.py     # HTTP endpoints (thin: receive request, call service)
    │   │   └── v1/               # Reserved for versioned API routes
    │   ├── core/
    │   │   └── config.py         # Settings loaded from environment variables
    │   ├── db/
    │   │   ├── base.py           # SQLAlchemy Base and the timestamp mixin
    │   │   └── session.py        # Engine, session factory and get_db dependency
    │   ├── models/               # SQLAlchemy models (Organisation, Site, User)
    │   ├── schemas/
    │   │   └── health.py         # Pydantic models: shape and validation of data
    │   └── services/
    │       └── health_service.py # Business logic (no HTTP knowledge)
    └── tests/
        ├── conftest.py           # Shared fixtures (test database, sessions)
        ├── test_health.py        # Health endpoint tests
        └── test_database.py      # Database, migration and relationship tests
```

### How the pieces connect

```
Request → uvicorn → main.py → route → service → database session → PostgreSQL
Response ← JSON    ←          ←       ←         ←
```

| Layer | Responsibility |
|---|---|
| **Route** | Receives the HTTP request and returns the response. Keeps no logic of its own. |
| **Schema** | Defines and validates the data going in and out of the API (Pydantic). |
| **Service** | Holds the business logic. Can be tested without a web server. |
| **Model** | Describes a database table (SQLAlchemy). |
| **Session** | One conversation with the database per request. Provided by `get_db`. |
| **Config** | Reads settings such as `DATABASE_URL` from the environment. No credentials in code. |

---

## Team workflow (Git)

Our agreed workflow:

```
develop → feature branch → implementation → pull request to develop → code review → approval and merge
```

Rules:

- Never commit directly to `main` or `develop`.
- Create every feature branch from the **latest `develop`**.
- One branch and one pull request per task. Open pull requests **targeting `develop`**.
- Do not force-push, and do not merge your own pull request.
- Do not delete files just to get rid of a merge conflict. Resolve it properly.
- Before every commit run `git status` and check that you are on the right branch and that `.env` is not listed.

Start a new piece of work:

```bash
git fetch origin
git checkout develop
git pull origin develop                       # always start from the latest develop
git checkout -b feature/short-description     # create your branch
# ...make changes...
git add <files>
git commit -m "Add site model tests"          # short, present tense
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

### Working together on one task branch

Several people can contribute to the same task. Everyone works on the **same branch**, and everything ends up in **one pull request**. The branch does not need to be merged for a teammate to use it: once it is pushed, it exists on GitHub.

**Joining an existing branch** (you need write access to the repository):

```bash
git fetch origin
git checkout feature/task-002-database-integration
git pull
```

Then set up your own environment: virtual environment, `pip install -r requirements.txt`, PostgreSQL user and databases, your own `.env`, and `python -m alembic upgrade head` (see [Setup](#setup) and [Database setup](#database-setup)).

**Every working session:**

```bash
git pull                     # get your teammates' latest work
# ...work, commit...
git pull                     # again, in case someone pushed meanwhile
git push
```

Habits that avoid conflicts:

- Agree in the group chat who owns which files before starting.
- Pull before you start and before you push. Say in the chat when you push.
- Never force-push or rewrite history on a shared branch.
- Only one person generates Alembic migrations on a branch.
- Pass work through Git (commit and push), not zip files or pasted code.
- Check that your commits carry your own identity: `git config user.name` and `git config user.email`.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'pydantic_settings'` (or another package) | The virtual environment is not active, or dependencies are not installed. Run `source .venv/bin/activate`, then `pip install -r requirements.txt`. Use `python -m alembic ...`, not a bare `alembic`. |
| `ModuleNotFoundError: No module named 'app'` | You are not in the `backend/` folder. Run `cd backend`. |
| `command not found: uvicorn` / `pytest` | The virtual environment is not active. Run `source .venv/bin/activate`. |
| `password authentication failed for user "hse_user"` | The password in `.env` does not match PostgreSQL. Reset it with `sudo -u postgres psql -c "ALTER USER hse_user WITH PASSWORD 'new_password';"` and update **both** URLs in `.env`. Test with the `psql` command in [Database setup](#4-check-the-connection). |
| The password in `.env` is correct but the app still uses another | A `DATABASE_URL` set in your shell overrides `.env`. Check with `env \| grep -i database_url`, then run `unset DATABASE_URL TEST_DATABASE_URL` and remove any `export` line from `~/.bashrc`. |
| `connection refused` on port 5432 | PostgreSQL is not running. Run `sudo service postgresql start`. |
| `database "hse_intelligence" does not exist` | Create it: `sudo -u postgres psql -c "CREATE DATABASE hse_intelligence OWNER hse_user;"` |
| `Field required` / validation error mentioning `database_url` | `.env` is missing or you are not in `backend/`. Run `cp .env.example .env` and fill it in. |
| Database tests show `skipped` | `TEST_DATABASE_URL` is not set in `.env`. |
| `Multiple head revisions are present` | Two migrations were created from the same parent. Tell the team, and do not delete either file. They need to be merged properly with `python -m alembic merge heads`. |
| `Address already in use` | Another server is on port 8000. Stop it, or run `uvicorn app.main:app --reload --port 8001`. |
| `git push` says the branch has no upstream | Run `git push -u origin <your-branch-name>` once. |
| Merge conflict after `git merge origin/develop` | Run `git status`, open each conflicted file, keep the correct content from both sides, then `git add` and `git commit`. To start over: `git merge --abort`. |
| `/favicon.ico 404` in the server log | Harmless. The browser is asking for a tab icon we don't have. |

---

## Roadmap

- [x] Task 001: FastAPI foundation, health check, schemas, service layer, tests
- [x] Task 002: PostgreSQL, SQLAlchemy models and Alembic migrations
- [ ] Task 003: Incident management module (report, list, view, update, delete)
- [ ] Authentication and role-based permissions
- [ ] React frontend integration
- [ ] AI-powered incident analysis
