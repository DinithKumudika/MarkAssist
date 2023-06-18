# routes
from fastapi import APIRouter

from routes.user import router as user_router
from routes.paper import router as paper_router
from routes.answer import router as answer_router

router = APIRouter()
# register routes
router.include_router(user_router, tags=["users"], prefix="/users")
router.include_router(paper_router,  tags=["papers"], prefix="/papers")
router.include_router(answer_router, tags=["answers"], prefix="/answers")