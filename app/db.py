import sqlalchemy
import databases
import os

# SQLAlchemy specific code, as with any other app
if os.getenv("DATABASE_URL"):
    # deployed in DigitalOcean
    DATABASE_URL = os.getenv("DATABASE_URL")
else:
    # local dev
    DATABASE_URL = "sqlite:///./test.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
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
