import os

# Must be set before `api.main` is imported: SuperTokens initialises at import time.
os.environ.setdefault("ST_API_KEY", "test-key")
os.environ.setdefault("GOOGLE_CLIENT_ID", "test-client-id.apps.googleusercontent.com")
