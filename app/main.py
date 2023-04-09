from fastapi import FastAPI
from api.routers import router as api_router
from models.base import Base, engine

app = FastAPI()

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(api_router)
