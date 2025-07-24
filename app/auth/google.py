# Source: https://medium.com/@vivekpemawat/enabling-googleauth-for-fast-api-1c39415075ea
# Source: https://deepwiki.com/fastapi-users/fastapi-users/7-oauth-integration
# Source: https://fastapi.tiangolo.com/tutorial/sql-databases/
# Source: https://fastapi.tiangolo.com/advanced/settings/

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from app.utils.oauth import get_google_auth, verify_google_token
from app.db.session import get_db
from app.db import crud
from sqlalchemy.orm import Session
from app.workers.celery_worker import log_login_event

router = APIRouter()


@router.get("/google-login")
async def login_google():
    google_auth = get_google_auth()
    authorization_base_url = "https://accounts.google.com/o/oauth2/auth"
    authorization_url, state = google_auth.authorization_url(authorization_base_url)
    return RedirectResponse(authorization_url)


from app.config import settings


@router.get("/google/callback")
async def google_callback(code: str, db: Session = Depends(get_db)):
    google_auth = get_google_auth()
    token_url = "https://oauth2.googleapis.com/token"
    token = google_auth.fetch_token(
        token_url=token_url,
        code=code,
        client_secret=settings.GOOGLE_CLIENT_SECRET
    )
    user_info = verify_google_token(token)
    user = crud.get_user_by_email(db, user_info.get("email"))
    if user:
        if user.provider != "google":
            raise HTTPException(
                status_code=400,
                detail="This email is already registered. Please log in with email and password."
            )
        user = crud.update_user_oauth(
            db, user=user, name=user_info.get("name"), provider_id=user_info.get("sub")
        )
    else:
        user = crud.create_user_oauth(
            db,
            email=user_info.get("email"),
            name=user_info.get("name"),
            provider="google",
            provider_id=user_info.get("sub"),
        )
    log_login_event.delay(user.email, "google")
    return {
        "user_info": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "provider": user.provider,
            "provider_id": user.provider_id,
        }
    }
