from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.db import database

router = APIRouter()


@router.get("/")
async def healthcheck():
    cause = []

    resp = await database.fetch_one("select 1")
    if resp[0] != 1:
        cause.append("BAD_DB")

    if len(cause) == 0:
        return {"status": "OK"}
    else:
        JSONResponse(
            status_code=500,
            content={"status": "DOWN", cause: cause},
        )
