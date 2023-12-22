from fastapi import FastAPI
import uvicorn

from microshop.users import router as users_router


app = FastAPI()
app.include_router(users_router)


@app.get("/")
async def get_root() -> str:
    return {"message": "Hello, World!"}


def start() -> None:
    """Launched with `poetry run start` at root level"""
    uvicorn.run("microshop.main:app", reload=True)
