from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class MatchRead(SQLModel):
    id: int
    api_fixture_id: int

    league_id: Optional[int] = None
    home_team_id: Optional[int] = None
    away_team_id: Optional[int] = None

    match_date: datetime

    status_long: Optional[str] = None
    status_short: Optional[str] = None
    elapsed: Optional[int] = None

    home_goals: Optional[int] = None
    away_goals: Optional[int] = None

    venue_names: Optional[str] = None
    venue_city: Optional[str] = None