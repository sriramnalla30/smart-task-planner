from __future__ import annotations

import logging
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.schemas import PlanRequest, PlanResponse
from app.services.plan_service import PlanService

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(
    title="Smart Task Planner API",
    description="AI-powered task planning service that breaks down goals into actionable plans",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_service() -> PlanService:
    settings = get_settings()
    return PlanService()


@app.post("/plan", response_model=PlanResponse, summary="Generate an execution plan")
async def create_plan(
    payload: PlanRequest,
    service: PlanService = Depends(get_service),
) -> PlanResponse:
    try:
        return await service.generate(payload)
    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(exc),
        ) from exc


@app.get("/health", summary="Simple service health check")
async def health() -> dict[str, str]:
    settings = get_settings()
    service = PlanService()
    return {
        "status": "ok",
        "provider": service.provider_name(),
        "app": settings.app_name,
    }
