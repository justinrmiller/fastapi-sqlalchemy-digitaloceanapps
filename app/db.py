import sqlalchemy
import databases
import os

if os.getenv("DATABASE_URL"):
    # deployed in DigitalOcean
    database_url = os.getenv("DATABASE_URL")
    database = databases.Database(database_url)
    engine = sqlalchemy.create_engine(
        database_url
    )
else:
    # local dev
    database_url = "sqlite:///./test.db"
    database = databases.Database(database_url)
    engine = sqlalchemy.create_engine(
        database_url,
        connect_args={"check_same_thread": False}
    )

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

# create tables if they're missing from the database
metadata.create_all(engine)
