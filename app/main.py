from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.db.session import get_db
from app.auth.routes import router as auth_router

app = FastAPI(
    title="FastAPI OAuth Backend",
    description="A FastAPI OAuth backend with Google and Facebook authentication",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def handle_exception(request: Request, exc: Exception):
    return JSONResponse({"error": str(exc)}, status_code=500)

app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI OAuth2 backend!"}