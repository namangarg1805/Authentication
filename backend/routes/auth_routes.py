from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from backend.config import KEYCLOAK_URL, CLIENT_ID, REDIRECT_URI, FRONTEND_URL
from backend.auth import exchange_code_for_token, refresh_access_token

router = APIRouter()

@router.get("/login")
def login():
    url = (
        f"{KEYCLOAK_URL}/protocol/openid-connect/auth"
        f"?client_id={CLIENT_ID}"
        f"&response_type=code"
        f"&scope=openid"
        f"&redirect_uri={REDIRECT_URI}"
    )
    return RedirectResponse(url)

@router.get("/callback")
def callback(code: str):
    tokens = exchange_code_for_token(code)

    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")

    response = RedirectResponse(url=FRONTEND_URL)

    # cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  
        samesite="lax"
    )

    # Refresh token cookie
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="lax"
    )

    return response

@router.get("/refresh")
def refresh(request):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        return {"error": "No refresh token"}

    tokens = refresh_access_token(refresh_token)

    response = RedirectResponse(url=FRONTEND_URL)

    response.set_cookie(
        key="access_token",
        value=tokens.get("access_token"),
        httponly=True,
        secure=False,
        samesite="lax"
    )

    return response

@router.get("/logout")
def logout():
    logout_url = (
        f"{KEYCLOAK_URL}/protocol/openid-connect/logout"
        f"?redirect_uri=http://localhost:8000/"
    )

    response = RedirectResponse(url=logout_url)

    # Delete local cookies
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")

    return response