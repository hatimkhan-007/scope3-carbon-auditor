from fastapi import FastAPI

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