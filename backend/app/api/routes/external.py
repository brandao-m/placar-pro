from datetime import date

import httpx
from fastapi import APIRouter, HTTPException, Query

from app.core.config import settings
from app.services.football_api_service import FootballApiService


router = APIRouter(
    prefix="/external",
    tags=["External Football API"],
)


@router.get("/fixtures")
def get_external_fixtures(
    fixture_date: date = Query(alias="date"),
):
    if not settings.FOOTBALL_API_KEY:
        raise HTTPException(
            status_code=400,
            detail="FOOTBALL_API_KEY não configurada no arquivo .env.",
        )

    service = FootballApiService()

    try:
        return service.get_fixtures_by_date(fixture_date=fixture_date)

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail="Erro ao consultar a API externa de futebol.",
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar à API externa de futebol.",
        )