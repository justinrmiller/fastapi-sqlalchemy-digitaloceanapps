from fastapi import FastAPI

from loguru import logger

app = FastAPI()


@app.get("/")
def root():
    logger.info("root called")
    return {"msg": "Hello World"}


@app.get("/healthcheck")
def healthcheck():
    logger.info("healthcheck called")
    return {"status": "OK"}
