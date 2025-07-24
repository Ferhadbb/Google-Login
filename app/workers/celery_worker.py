
# Source: https://testdriven.io/blog/fastapi-celery/
from celery import Celery
from app.config import settings

celery = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)

@celery.task
def log_login_event(email, provider):
    # Just print, in real life you'd log to DB or file
    print(f"User {email} logged in with {provider}")