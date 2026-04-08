# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse

# # Import routes
# from backend.routes import auth_routes, protected_routes

# app = FastAPI()

# # ---------------------------
# # CORS (allow frontend calls)
# # ---------------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # for development only
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # ---------------------------
# # Serve frontend (static files)
# # ---------------------------
# app.mount("/static", StaticFiles(directory="frontend"), name="static")


# # ---------------------------
# # Serve index.html at root
# # ---------------------------
# @app.get("/")
# def serve_frontend():
#     return FileResponse("frontend/index.html")


# # ---------------------------
# # Include API routes
# # ---------------------------
# app.include_router(auth_routes.router)
# app.include_router(protected_routes.router)


# # ---------------------------
# # Health check
# # ---------------------------
# @app.get("/health")
# def health():
#     return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.routes import auth_routes, protected_routes

app = FastAPI()

# CORS (for cookies)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")


@app.get("/")
def serve_frontend():
    return FileResponse("frontend/index.html")


# Routes
app.include_router(auth_routes.router)
app.include_router(protected_routes.router)


@app.get("/health")
def health():
    return {"status": "ok"}