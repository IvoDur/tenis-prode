from fastapi import FastAPI
from routes.users import user_router
from routes.matches import match_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user_router)
app.include_router(match_router)

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
