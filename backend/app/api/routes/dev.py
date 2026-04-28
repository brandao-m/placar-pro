from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.league import League
from app.models.match import Match
from app.models.team import Team


router = APIRouter(
    prefix="/dev",
    tags=["Development"],
)


@router.post("/seed")
def seed_database(
    session: Annotated[Session, Depends(get_session)],
):
    existing_match = session.exec(
        select(Match).where(Match.api_fixture_id == 1001)
    ).first()

    if existing_match:
        return {
            "message": "Dados de teste já existem no banco."
        }

    league = League(
        api_league_id=71,
        name="Brasileirão Série A",
        country="Brasil",
        logo_url="https://media.api-sports.io/football/leagues/71.png",
        season=2026,
    )

    home_team = Team(
        api_team_id=127,
        name="Flamengo",
        country="Brasil",
        logo_url="https://media.api-sports.io/football/teams/127.png",
        founded=1895,
    )

    away_team = Team(
        api_team_id=121,
        name="Palmeiras",
        country="Brasil",
        logo_url="https://media.api-sports.io/football/teams/121.png",
        founded=1914,
    )

    session.add(league)
    session.add(home_team)
    session.add(away_team)

    session.commit()

    session.refresh(league)
    session.refresh(home_team)
    session.refresh(away_team)

    match = Match(
        api_fixture_id=1001,
        league_id=league.id,
        home_team_id=home_team.id,
        away_team_id=away_team.id,
        match_date=datetime(2026, 4, 28, 20, 0, tzinfo=timezone.utc),
        status_long="Not Started",
        status_short="NS",
        elapsed=None,
        home_goals=None,
        away_goals=None,
        venue_name="Maracanã",
        venue_city="Rio de Janeiro",
    )

    session.add(match)
    session.commit()
    session.refresh(match)

    return {
        "message": "Dados de teste criados com sucesso.",
        "league_id": league.id,
        "home_team_id": home_team.id,
        "away_team_id": away_team.id,
        "match_id": match.id,
    }