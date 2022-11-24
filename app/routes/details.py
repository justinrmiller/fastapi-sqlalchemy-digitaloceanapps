from fastapi import APIRouter
import os

from app.models.details import (
    Details
)

router = APIRouter()


@router.get("/", response_model=Details)
async def details():
    env = os.environ["ENV"]
    version = os.environ['VERSION']

    return {
        "env": env,
        "version": version,
    }
