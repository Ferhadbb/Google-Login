# Source: https://developers.facebook.com/docs/facebook-login/
# Source: https://deepwiki.com/fastapi-users/fastapi-users/7-oauth-integration
# Source: https://fastapi.tiangolo.com/tutorial/sql-databases/
# Source: https://fastapi.tiangolo.com/advanced/settings/

from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from app.utils.oauth import get_facebook_auth, verify_facebook_token
from app.db.session import get_db
from app.db import crud
from sqlalchemy.orm import Session
from app.workers.celery_worker import log_login_event

router = APIRouter()

@router.get("/facebook-login")
async def login_facebook():
    facebook_auth = get_facebook_auth()
    authorization_base_url = "https://www.facebook.com/v10.0/dialog/oauth"
    authorization_url, state = facebook_auth.authorization_url(authorization_base_url)
    return RedirectResponse(authorization_url)

@router.get("/facebook/callback")
async def facebook_callback(code: str, db: Session = Depends(get_db)):
    facebook_auth = get_facebook_auth()
    token = facebook_auth.fetch_token(code=code)
    user_info = verify_facebook_token(token)
    user = crud.get_user_by_email(db, user_info.get("email"))
    if not user:
        user = crud.create_user_oauth(
            db,
            email=user_info.get("email"),
            name=user_info.get("name"),
            provider="facebook",
            provider_id=user_info.get("id")
        )
    else:
        user = crud.update_user_oauth(
            db,
            user=user,
            name=user_info.get("name"),
            provider_id=user_info.get("id")
        )
    log_login_event.delay(user.email, "facebook")
    return {
        "user_info": {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "provider": user.provider,
            "provider_id": user.provider_id
        }
    }