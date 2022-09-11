from fastapi import Depends, Security, APIRouter

from app.models.users import User
from app.utils.users import (
    get_current_active_user
)

# from app.db import database, users

router = APIRouter()


@router.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.get("/users/me/items")
async def read_own_items(
    current_user: User = Security(get_current_active_user, scopes=["items"])
):
    return [{"item_id": "Foo", "owner": current_user.username}]


# @router.get("/status/")
# async def read_system_status(current_user: User = Depends(get_current_user)):
#     return {"status": "ok"}
