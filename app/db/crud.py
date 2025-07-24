# Source: https://fastapi.tiangolo.com/tutorial/sql-databases/
# Source: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# Source: https://fastapi.tiangolo.com/advanced/settings/

from sqlalchemy.orm import Session
from app.db.models import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user_oauth(db: Session, email: str, name: str, provider: str, provider_id: str):
    user = User(email=email, name=name, provider=provider, provider_id=provider_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def update_user_oauth(db: Session, user: User, name: str, provider_id: str):
    user.name = name
    user.provider_id = provider_id
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if not user or not user.hashed_password:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_user_with_password(db: Session, email: str, password: str, name: str = ""):
    hashed_password = pwd_context.hash(password)
    user = User(email=email, name=name, provider="local", provider_id=email, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user