from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from microshop.users import router as users_router
from microshop.api_v1 import router as api_v1_router
from microshop.core.models import Base, db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app: FastAPI = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(api_v1_router)


@app.get("/")
async def get_root() -> str:
    return {"message": "Hello, World!"}


def start() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("microshop.main:app", reload=True)
