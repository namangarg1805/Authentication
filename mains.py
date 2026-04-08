# from fastapi import FastAPI, Header, HTTPException
# from fastapi.responses import RedirectResponse
# from jose import jwt
# import requests

# app = FastAPI()

# KEYCLOAK_URL = "http://localhost:8080/realms/demo"
# CLIENT_ID = "fastapi-client"

# # ------------------------
# # Fetch public keys (JWKS)
# # ------------------------
# jwks = requests.get(f"{KEYCLOAK_URL}/protocol/openid-connect/certs").json()


# # ------------------------
# # 1. Login → Redirect to Keycloak
# # ------------------------
# @app.get("/login")
# def login():
#     url = (
#         f"{KEYCLOAK_URL}/protocol/openid-connect/auth"
#         f"?client_id={CLIENT_ID}"
#         f"&response_type=code"
#         f"&scope=openid"
#         f"&redirect_uri=http://localhost:8000/callback"
#     )
#     return RedirectResponse(url)


# # ------------------------
# # 2. Callback → Exchange Code for Tokens
# # ------------------------
# @app.get("/callback")
# def callback(code: str):
#     token_url = f"{KEYCLOAK_URL}/protocol/openid-connect/token"

#     data = {
#         "grant_type": "authorization_code",
#         "client_id": CLIENT_ID,
#         "code": code,
#         "redirect_uri": "http://localhost:8000/callback"
#     }

#     tokens = requests.post(token_url, data=data).json()

#     return {
#         "access_token": tokens.get("access_token"),
#         "id_token": tokens.get("id_token")
#     }


# # ------------------------
# # 3. Verify JWT
# # ------------------------
# def verify_token(token: str):
#     try:
#         header = jwt.get_unverified_header(token)
#         key = next(k for k in jwks["keys"] if k["kid"] == header["kid"])

#         payload = jwt.decode(
#             token,
#             key,
#             algorithms=["RS256"],
#             options={
#                 "verify_aud": False   #
#             }
#         )

#         return payload

#     except Exception as e:
#         print("ERROR:", str(e))
#         raise HTTPException(status_code=401, detail="Invalid token")

# # ------------------------
# # 4. Protected API
# # ------------------------
# @app.get("/protected")
# def protected(authorization: str = Header(...)):
#     token = authorization.split(" ")[1]
#     user = verify_token(token)

#     return {
#         "message": "Access granted",
#         "user": user
#     }