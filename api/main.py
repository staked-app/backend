import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from supertokens_python import get_all_cors_headers
from supertokens_python.framework.fastapi import get_middleware

from starlette.responses import RedirectResponse
from api import config
from api.routes import auth, users
from api.routes.debug import protected

app = FastAPI(title="STAKED API")
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(protected.router)

app.add_middleware(get_middleware())
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type"] + get_all_cors_headers(),
    expose_headers=get_all_cors_headers(),
)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
