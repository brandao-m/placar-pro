from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Match(SQLModel, table=True):
    __tablename__ = "football_match"

    id: Optional[int] = Field(default=None, primary_key=True)

    api_fixture_id: int = Field(index=True, unique=True)

    league_id: Optional[int] = Field(default=None, foreign_key="league.id")
    home_team_id: Optional[int] = Field(default=None, foreign_key="team.id")
    away_team_id: Optional[int] = Field(default=None, foreign_key="team.id")

    match_date: datetime

    status_long: Optional[str] = None
    status_short: Optional[str] = None
    elapsed: Optional[int] = None

    home_goals: Optional[int] = None
    away_goals: Optional[int] = None

    venue_name: Optional[str] = None
    venue_city: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)