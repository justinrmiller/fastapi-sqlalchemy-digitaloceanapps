from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello World"}


@app.get("/healthcheck")
def healthcheck():
    return {"status": "OK"}
