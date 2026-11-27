import pytest
from sqlalchemy import inspect, text
from sqlalchemy.exc import IntegrityError

from app.models import Organisation, Site, User


def test_database_connection(db_session):
    assert db_session.execute(text("SELECT 1")).scalar() == 1


def test_migrations_created_tables(migrated_engine):
    tables = set(inspect(migrated_engine).get_table_names())
    assert {"organisations", "sites", "users"} <= tables


def test_relationships(db_session):
    org = Organisation(name="Acme Oil")
    site = Site(name="Lagos Terminal", organisation=org)
    user = User(email="ada@acme.test", full_name="Ada", organisation=org, site=site)
    db_session.add_all([org, site, user])
    db_session.flush()

    assert site in org.sites
    assert user in org.users
    assert user in site.users
    assert user.organisation_id == org.id


def test_duplicate_email_rejected(db_session):
    org = Organisation(name="Acme Oil")
    db_session.add(org)
    db_session.flush()
    db_session.add(User(email="a@acme.test", full_name="A", organisation_id=org.id))
    db_session.add(User(email="a@acme.test", full_name="B", organisation_id=org.id))
    with pytest.raises(IntegrityError):
        db_session.flush()