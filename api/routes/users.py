from fastapi import APIRouter, Depends, HTTPException
from supertokens_python.asyncio import get_user
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def me(session: SessionContainer = Depends(verify_session())):
    """Profile of the signed-in user. The app calls this right after login."""
    user = await get_user(session.get_user_id())
    if user is None:
        # Session outlived the user (e.g. account deleted): treat as signed out.
        raise HTTPException(status_code=401, detail="User no longer exists")

    providers = sorted(
        {
            lm.third_party.id if lm.recipe_id == "thirdparty" and lm.third_party else lm.recipe_id
            for lm in user.login_methods
        }
    )
    return {
        "id": user.id,
        "email": user.emails[0] if user.emails else None,
        "providers": providers,
        "time_joined": user.time_joined,
    }
