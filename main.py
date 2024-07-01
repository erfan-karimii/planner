from fastapi import FastAPI
from routes.users import user_router
import uvicorn


app = FastAPI()
# Register routes
app.include_router(user_router, prefix="/user",tags=['user'])


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)