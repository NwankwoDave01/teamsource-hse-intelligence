import os
import subprocess
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

BACKEND_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BACKEND_DIR / ".env")


@pytest.fixture(scope="session")
def test_database_url() -> str:
    url = os.environ.get("TEST_DATABASE_URL")
    if not url:
        pytest.skip("TEST_DATABASE_URL is not set")
    return url


@pytest.fixture(scope="session")
def migrated_engine(test_database_url):
    """Run the real Alembic migrations on the TEST database, once per test run."""
    env = {**os.environ, "DATABASE_URL": test_database_url}
    alembic = [sys.executable, "-m", "alembic"]
    subprocess.run([*alembic, "upgrade", "head"], cwd=BACKEND_DIR, env=env, check=True)
    engine = create_engine(test_database_url)
    yield engine
    engine.dispose()
    subprocess.run([*alembic, "downgrade", "base"], cwd=BACKEND_DIR, env=env, check=True)


@pytest.fixture
def db_session(migrated_engine):
    """A session whose changes are rolled back after every test."""
    connection = migrated_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection, join_transaction_mode="create_savepoint")
    yield session
    session.close()
    transaction.rollback()
    connection.close()