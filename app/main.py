from fastapi import FastAPI

from app.routers import validation
from app.services.supabase_service import supabase
from fastapi.staticfiles import StaticFiles
from pathlib import Path

print("Supabase conectado:", supabase is not None)

app = FastAPI(
    title="Vividly Backend",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parents[1]

app.mount(
    "/storage",
    StaticFiles(directory=BASE_DIR / "storage"),
    name="storage",
)

app.include_router(
    validation.router,
    prefix="/validation",
    tags=["Validation"]
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Vividly Backend!"
    }