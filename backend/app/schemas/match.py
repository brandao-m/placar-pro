from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class MatchTeamRead(SQLModel):
    id: int
    name: str
    logo_url: Optional[str] = None


class MatchLeagueRead(SQLModel):
    id: int
    name: str
    country: Optional[str] = None
    logo_url: Optional[str] = None
    season: Optional[int] = None


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

    venue_name: Optional[str] = None
    venue_city: Optional[str] = None


class MatchListRead(SQLModel):
    id: int
    api_fixture_id: int
    match_date: datetime

    status_long: Optional[str] = None
    status_short: Optional[str] = None
    elapsed: Optional[int] = None

    home_goals: Optional[int] = None
    away_goals: Optional[int] = None

    venue_name: Optional[str] = None
    venue_city: Optional[str] = None

    league: Optional[MatchLeagueRead] = None
    home_team: Optional[MatchTeamRead] = None
    away_team: Optional[MatchTeamRead] = None