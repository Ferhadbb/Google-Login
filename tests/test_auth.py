
# Source: https://fastapi.tiangolo.com/tutorial/testing/
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_google_login_redirect():
    response = client.get("/auth/google-login")
    assert response.status_code == 307 or response.status_code == 302

def test_facebook_login_redirect():
    response = client.get("/auth/facebook-login")
    assert response.status_code == 307 or response.status_code == 302

def test_google_login_redirect():
    response = client.get("/auth/google-login")
    print("Google login response:", response.status_code, response.text)
    assert response.status_code == 307 or response.status_code == 302

def test_facebook_login_redirect():
    response = client.get("/auth/facebook-login")
    print("Facebook login response:", response.status_code, response.text)
    assert response.status_code == 307 or response.status_code == 302