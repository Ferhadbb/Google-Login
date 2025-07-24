# FastAPI OAuth Backend

A production-ready FastAPI backend with Google and Facebook OAuth2 login, JWT authentication, PostgreSQL, Redis, Celery, RabbitMQ, and Alembic migrations. Includes Docker support and example tests.

---

## Features

- Google Login via OAuth2
- Facebook Login via OAuth2
- JWT Authentication (email/password)
- User registration and login
- PostgreSQL database (via Docker)
- Redis for caching
- Celery + RabbitMQ for background tasks
- Alembic for database migrations
- Docker & Docker Compose for easy setup
- Unit tests with pytest

---

## Quickstart

### 1. **Clone and configure**
```sh
git clone <your-repo-url>
cd fastapi-oauth-backend
cp .env.example .env
# Edit .env with your OAuth credentials and secrets
```

### 2. **Build and run with Docker**
```sh
docker-compose up --build
```

### 3. **Visit**
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### 4. **Run tests**
```sh
docker-compose run --rm app pytest
```

---

## Database Migrations

- **Create migration:**  
  ```sh
  docker-compose run --rm app alembic revision --autogenerate -m "Migration message"
  ```
- **Apply migration:**  
  ```sh
  docker-compose run --rm app alembic upgrade head
  ```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your secrets:
```
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/socialauth
SECRET_KEY=your-secret-key
GOOGLE_CLIENT_ID=...
GOOGLE_CLIENT_SECRET=...
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback
FACEBOOK_CLIENT_ID=...
FACEBOOK_CLIENT_SECRET=...
FACEBOOK_REDIRECT_URI=http://localhost:8000/auth/facebook/callback
REDIS_HOST=redis
REDIS_PORT=6379
RABBITMQ_HOST=rabbitmq
RABBITMQ_PORT=5672
CELERY_BROKER_URL=amqp://guest:guest@rabbitmq:5672//
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

---

## Project Structure

```
fastapi-oauth-backend/
  app/
    auth/
    db/
    models/
    routes/
    utils/
    ...
  tests/
  alembic/
  alembic.ini
  Dockerfile
  docker-compose.yml
  requirements.txt
  README.md
```

---

## License

MIT (or your choice)

---

## Credits

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Celery](https://docs.celeryq.dev/)
- [Docker](https://www.docker.com/)

---

## Sources & Tutorials

- [FastAPI Security: OAuth2 with Password (and hashing), Bearer with JWT tokens](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/)
- [FastAPI SQL (Relational) Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)
- [FastAPI: Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/tutorial/bigger-applications/)
- [FastAPI Advanced Settings](https://fastapi.tiangolo.com/advanced/settings/)
- [Google OAuth for FastAPI (Medium)](https://medium.com/@vivekpemawat/enabling-googleauth-for-fast-api-1c39415075ea)
- [FastAPI Users: OAuth Integration (DeepWiki)](https://deepwiki.com/fastapi-users/fastapi-users/7-oauth-integration)
- [TestDriven.io: FastAPI + Celery](https://testdriven.io/blog/fastapi-celery/)
- [Facebook Login Documentation](https://developers.facebook.com/docs/facebook-login/) 