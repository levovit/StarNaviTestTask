from fastapi import FastAPI
from api.routers import router as api_router
from models.base import Base, engine
from utils.logger_utils import get_logger

app = FastAPI()

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app.include_router(api_router)

logger = get_logger('startups')


@app.on_event("startup")
async def startup_event():
    logger.info("Application started.")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application ended.")
