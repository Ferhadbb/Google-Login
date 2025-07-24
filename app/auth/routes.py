# Source: https://fastapi.tiangolo.com/tutorial/bigger-applications/
from fastapi import APIRouter

from app.auth import google, facebook, jwt

router = APIRouter()

# Google OAuth2 routes
router.include_router(google.router, prefix="/auth", tags=["Google Auth"])

# Facebook OAuth2 routes
router.include_router(facebook.router, prefix="/auth", tags=["Facebook Auth"])

# JWT Auth route
router.include_router(jwt.router, prefix="/auth", tags=["JWT"])