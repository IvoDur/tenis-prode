from fastapi import FastAPI
from routes.users import user_router
from routes.matches import match_router

app = FastAPI()

app.include_router(user_router)
app.include_router(match_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
