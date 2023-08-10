from fastapi import FastAPI

from app.api.models import entity, feed, media, author
from app.api.routers import router
from app.core.database import engine

entity.Base.metadata.create_all(bind=engine)
author.Base.metadata.create_all(bind=engine)
feed.Base.metadata.create_all(bind=engine)
media.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
