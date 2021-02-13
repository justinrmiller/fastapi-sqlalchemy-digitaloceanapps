import os

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
