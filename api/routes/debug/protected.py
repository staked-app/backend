from fastapi import Depends, APIRouter
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session

router = APIRouter(prefix="/debug")

@router.get("/me")
async def me(session: SessionContainer = Depends(verify_session())):
    return {"user_id": session.get_user_id()}