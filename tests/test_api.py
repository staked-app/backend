from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_users_me_requires_session():
    # No tokens at all -> SuperTokens rejects before ever contacting the core.
    res = client.get("/users/me", headers={"st-auth-mode": "header"})
    assert res.status_code == 401


def test_debug_me_requires_session():
    assert client.get("/debug/me").status_code == 401


def test_auth_routes_are_served_by_supertokens():
    assert "/users/me" in client.get("/openapi.json").json()["paths"]
    # Unknown body on a SuperTokens endpoint should be handled by the middleware (4xx), not 404.
    res = client.post("/auth/signin", json={})
    assert res.status_code != 404


def test_cors_exposes_session_headers():
    res = client.options(
        "/users/me",
        headers={
            "Origin": "http://localhost:3000",
            "Access-Control-Request-Method": "GET",
            "Access-Control-Request-Headers": "st-auth-mode,authorization",
        },
    )
    assert res.status_code == 200
    assert res.headers["access-control-allow-origin"] == "http://localhost:3000"
