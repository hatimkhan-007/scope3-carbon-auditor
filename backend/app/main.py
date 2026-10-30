from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine

app = FastAPI(
    title="OmniScope AI",
    description="Scope 3 Carbon Emissions Management Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to OmniScope AI",
        "Status": "Running",
        "Version": "1.0.0"
    }

@app.get("/health")
def health_check():
    return {
        "Status": "healthy"
    }

@app.get("/db-health")
def database_health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "connected",
            "database": "PostgreSQL"
        }
    except Exception as error:
        return {
            "status": "error",
            "message": str(error)
        }