import requests
from jose import jwt
from fastapi import HTTPException
from backend.config import KEYCLOAK_URL, CLIENT_ID, REDIRECT_URI

jwks = requests.get(f"{KEYCLOAK_URL}/protocol/openid-connect/certs").json()


def verify_token(token: str):
    try:
        header = jwt.get_unverified_header(token)
        key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])

        payload = jwt.decode(
            token,
            key,
            algorithms=["RS256"],
            options={"verify_aud": False}
        )

        return payload

    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=401, detail="Invalid token")


def exchange_code_for_token(code: str):
    token_url = f"{KEYCLOAK_URL}/protocol/openid-connect/token"

    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    return requests.post(token_url, data=data).json()


def refresh_access_token(refresh_token: str):
    token_url = f"{KEYCLOAK_URL}/protocol/openid-connect/token"

    data = {
        "grant_type": "refresh_token",
        "client_id": CLIENT_ID,
        "refresh_token": refresh_token
    }

    return requests.post(token_url, data=data).json()