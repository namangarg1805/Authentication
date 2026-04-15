from fastapi import APIRouter, Depends
from backend.dependencies import get_current_user, require_admin

router = APIRouter()


@router.get("/protected")
def protected(user=Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": user
    }


@router.get("/admin")
def admin(user=Depends(get_current_user)):
    require_admin(user)

    return {
        "message": "Admin access granted",
        "user": user
    }