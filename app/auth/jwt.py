# Source: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# Source: https://fastapi.tiangolo.com/tutorial/sql-databases/
# Source: https://fastapi.tiangolo.com/tutorial/bigger-applications/
# Source: https://fastapi.tiangolo.com/advanced/settings/
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.db.session import get_db
from app.db import crud
from sqlalchemy.orm import Session
from app.auth.jwt_utils import create_access_token
from fastapi import Body

router = APIRouter()

@router.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register")
def register_user(
    email: str = Body(...),
    password: str = Body(...),
    name: str = Body("")
    , db: Session = Depends(get_db)
):
    existing_user = crud.get_user_by_email(db, email)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )
    user = crud.create_user_with_password(db, email, password, name)
    return {"message": "User registered successfully", "user_id": user.id}