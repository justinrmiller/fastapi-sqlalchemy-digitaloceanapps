from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    return {"msg": "Hello World"}
