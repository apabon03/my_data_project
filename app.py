from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
from core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient #librería para manejo de bd asynncrona



app = FastAPI(
    title=settings.PROJECT_NAME,
    description="This is a simple RestApi",
    version="0.0.1",
    openapi_tags=tags_metadata
)

app.include_router(user)