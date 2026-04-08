# from fastapi import Header, HTTPException
# from backend.auth import verify_token


# def get_current_user(authorization: str = Header(...)):
#     try:
#         token = authorization.split(" ")[1]
#         return verify_token(token)
#     except Exception:
#         raise HTTPException(status_code=401, detail="Invalid auth header")


# def require_admin(user):
#     roles = user.get("realm_access", {}).get("roles", [])

#     if "admin" not in roles:
#         raise HTTPException(status_code=403, detail="Admin only")

from fastapi import Request, HTTPException
from backend.auth import verify_token


def get_current_user(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    return verify_token(token)


def require_admin(user):
    roles = user.get("realm_access", {}).get("roles", [])

    if "admin" not in roles:
        raise HTTPException(status_code=403, detail="Admin only")