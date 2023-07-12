from fastapi import APIRouter
from .endpoints import feed, user

# Create the main API router
router = APIRouter()

# Include individual endpoint routers
router.include_router(user.router, prefix="/users", tags=["Users"])
router.include_router(feed.router, prefix="/feeds", tags=["Feeds"])


# Export the main API router
__all__ = ["router"]
