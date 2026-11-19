"""Central, environment-driven configuration for the STAKED API."""

import os


def _csv(name: str, default: str) -> list[str]:
    return [v.strip() for v in os.environ.get(name, default).split(",") if v.strip()]


# Public URL of this API. The mobile app talks to it directly.
API_DOMAIN = os.environ.get("API_DOMAIN", "http://localhost:8000")

# SuperTokens requires a website domain even for a mobile-only client.
WEBSITE_DOMAIN = os.environ.get("WEBSITE_DOMAIN", "http://localhost:2000")

SUPERTOKENS_URI = os.environ.get("SUPERTOKENS_URI", "http://localhost:3567")
SUPERTOKENS_API_KEY = os.environ["ST_API_KEY"]

# Google OAuth.
# GOOGLE_CLIENT_ID must be the *web / server* client ID. The Flutter app passes the
# same value as `serverClientId` to google_sign_in so that the ID token it sends to
# /auth/signinup has this value as its audience.
GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
# Only needed for the browser redirect (authorization code) flow, not for the native one.
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET") or None

# Browser origins allowed to call the API (only relevant for Flutter web / admin tools).
CORS_ORIGINS = _csv("CORS_ORIGINS", "http://localhost:3000,http://localhost:2000")
