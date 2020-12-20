import sqlalchemy
import databases
import os

metadata = sqlalchemy.MetaData()

if os.getenv("database_url"):
    # deployed in DigitalOcean
    database_url = os.getenv("database_url")
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

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

# create tables if they're missing from the database
metadata.create_all(engine)
