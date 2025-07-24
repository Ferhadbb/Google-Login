# Source: https://medium.com/@vivekpemawat/enabling-googleauth-for-fast-api-1c39415075ea
# Source: https://deepwiki.com/fastapi-users/fastapi-users/7-oauth-integration
# Source: https://developers.facebook.com/docs/facebook-login/
# Source: https://fastapi.tiangolo.com/advanced/settings/

from requests_oauthlib import OAuth2Session
from app.config import settings
import requests

GOOGLE_SCOPES = [
    "openid",
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile"
]

def get_google_auth():
    return OAuth2Session(
        client_id=settings.GOOGLE_CLIENT_ID,
        redirect_uri=settings.GOOGLE_REDIRECT_URI,
        scope=GOOGLE_SCOPES
    )

def verify_google_token(token):
    resp = requests.get("https://www.googleapis.com/oauth2/v3/userinfo", headers={
        "Authorization": f"Bearer {token['access_token']}"
    })
    return resp.json()

def get_facebook_auth():
    return OAuth2Session(
        client_id=settings.FACEBOOK_CLIENT_ID,
        redirect_uri=settings.FACEBOOK_REDIRECT_URI,
        scope=["email", "public_profile"]
    )

def verify_facebook_token(token):
    resp = requests.get(
        "https://graph.facebook.com/me",
        params={
            "fields": "id,name,email",
            "access_token": token["access_token"]
        }
    )
    return resp.json()