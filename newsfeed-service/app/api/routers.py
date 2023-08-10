from fastapi import APIRouter
from .endpoints import feed, author, entity

# Create the main API router
router = APIRouter()

# Include individual endpoint routers
router.include_router(author.router, prefix="/authors", tags=["Authors"])
router.include_router(entity.router, prefix="/entities", tags=["Entities"])
router.include_router(feed.router, prefix="/feeds", tags=["Feeds"])


# Export the main API router
__all__ = ["router"]
