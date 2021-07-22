import sqlalchemy
import databases
import os
import ssl

if os.getenv("DATABASE_URL"):
    # deployed in DigitalOcean
    database_url = os.getenv("DATABASE_URL")

    # have to disable cert verification due to DigitalOcean's use of self-signed certs
    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.verify_mode = ssl.CERT_NONE
    database = databases.Database(database_url, ssl=context)

    engine = sqlalchemy.create_engine(
        database_url,
        connect_args={"sslmode": "require"}
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
