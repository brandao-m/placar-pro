from datetime import date
from typing import Any

import httpx

from app.core.config import settings


class FootballApiService:
    def __init__(self):
        self.base_url = settings.FOOTBALL_API_BASE_URL
        self.headers = {
            "x-apisports-key": settings.FOOTBALL_API_KEY,
        }

    def get_fixtures_by_date(self, fixture_date: date) -> dict[str, Any]:
        url = f"{self.base_url}/fixtures"

        params = {
            "date": fixture_date.isoformat(),
        }

        response = httpx.get(
            url,
            headers=self.headers,
            params=params,
            timeout=15,
        )

        response.raise_for_status()

        return response.json()