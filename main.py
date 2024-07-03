from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn

from routes.users import user_router
from routes.events import event_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    conn()
    yield


app = FastAPI(lifespan=lifespan)

# Register routes
app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(event_router, prefix="/event")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
