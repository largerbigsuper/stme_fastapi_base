
from fastapi.staticfiles import StaticFiles
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.auth.api.v1.api import router
from apps.wes.api.v1.api import router as wes_router
from core.config import settings


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.APP_ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=settings.APP_ALLOW_METHODS,
    allow_headers=["*"],

)

app.include_router(router, prefix="/" + settings.API_V1_STR)
app.include_router(wes_router, prefix="/" + settings.API_V1_STR)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)