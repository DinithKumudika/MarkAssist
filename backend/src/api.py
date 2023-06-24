# routes
from fastapi import APIRouter

from routes.auth import router as auth_router
from routes.user import router as user_router
from routes.paper import router as paper_router
from routes.answer import router as answer_router
from routes.subject import router as subject_router

router = APIRouter()

# register routes
router.include_router(auth_router, tags=["authentication"], prefix="/auth")
router.include_router(user_router, tags=["users"], prefix="/users")
router.include_router(paper_router,  tags=["papers"], prefix="/papers")
router.include_router(answer_router, tags=["answers"], prefix="/answers")
router.include_router(subject_router, tags=["subjects"], prefix="/subjects")