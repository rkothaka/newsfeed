from fastapi import FastAPI
from app.core.database import engine, Base
from app.api.routers import router
from app.api.models import entity, feed, media, user

entity.Base.metadata.create_all(bind=engine)
feed.Base.metadata.create_all(bind=engine)
media.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
