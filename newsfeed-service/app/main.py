from fastapi import FastAPI
from app.core.database import engine
from app.api.routers import router
from app.api.models import feed

feed.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(router)