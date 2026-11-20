from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(
    title="HSE Intelligence API",
    description="AI-powered HSE Management and Incident Intelligence Platform",
    version="0.1.0",
)

app.include_router(health.router)