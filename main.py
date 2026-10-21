
from fastapi import FastAPI

app = FastAPI(
    title="ShieldDesk API",
    description="IT Helpdesk & Service Request Management",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "ShieldDesk Backend is running!",
        "status": "success",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }
