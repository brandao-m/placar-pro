from datetime import date, datetime, time, timezone
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.league import League
from app.models.match import Match
from app.models.team import Team
from app.schemas.match import (
    MatchLeagueRead,
    MatchListRead,
    MatchTeamRead,
)


router = APIRouter(
    prefix="/matches",
    tags=["Matches"],
)


@router.get("/", response_model=list[MatchListRead])
def list_matches(
    session: Annotated[Session, Depends(get_session)],
    match_date: date | None = Query(default=None, alias="date"),
):
    statement = select(Match)

    if match_date:
        start_of_day = datetime.combine(
            match_date,
            time.min,
            tzinfo=timezone.utc,
        )

        end_of_day = datetime.combine(
            match_date,
            time.max,
            tzinfo=timezone.utc,
        )

        statement = statement.where(
            Match.match_date >= start_of_day,
            Match.match_date <= end_of_day,
        )

    matches = session.exec(statement).all()

    response = []

    for match in matches:
        league = None
        home_team = None
        away_team = None

        if match.league_id:
            league_model = session.get(League, match.league_id)

            if league_model:
                league = MatchLeagueRead(
                    id=league_model.id,
                    name=league_model.name,
                    country=league_model.country,
                    logo_url=league_model.logo_url,
                    season=league_model.season,
                )

        if match.home_team_id:
            home_team_model = session.get(Team, match.home_team_id)

            if home_team_model:
                home_team = MatchTeamRead(
                    id=home_team_model.id,
                    name=home_team_model.name,
                    logo_url=home_team_model.logo_url,
                )

        if match.away_team_id:
            away_team_model = session.get(Team, match.away_team_id)

            if away_team_model:
                away_team = MatchTeamRead(
                    id=away_team_model.id,
                    name=away_team_model.name,
                    logo_url=away_team_model.logo_url,
                )

        response.append(
            MatchListRead(
                id=match.id,
                api_fixture_id=match.api_fixture_id,
                match_date=match.match_date,
                status_long=match.status_long,
                status_short=match.status_short,
                elapsed=match.elapsed,
                home_goals=match.home_goals,
                away_goals=match.away_goals,
                venue_name=match.venue_name,
                venue_city=match.venue_city,
                league=league,
                home_team=home_team,
                away_team=away_team,
            )
        )

    return response


@router.get("/{match_id}", response_model=MatchListRead)
def get_match_by_id(
    match_id: int,
    session: Annotated[Session, Depends(get_session)],
):
    match = session.get(Match, match_id)

    if not match:
        raise HTTPException(
            status_code=404,
            detail="Partida não encontrada.",
        )

    league = None
    home_team = None
    away_team = None

    if match.league_id:
        league_model = session.get(League, match.league_id)

        if league_model:
            league = MatchLeagueRead(
                id=league_model.id,
                name=league_model.name,
                country=league_model.country,
                logo_url=league_model.logo_url,
                season=league_model.season,
            )

    if match.home_team_id:
        home_team_model = session.get(Team, match.home_team_id)

        if home_team_model:
            home_team = MatchTeamRead(
                id=home_team_model.id,
                name=home_team_model.name,
                logo_url=home_team_model.logo_url,
            )

    if match.away_team_id:
        away_team_model = session.get(Team, match.away_team_id)

        if away_team_model:
            away_team = MatchTeamRead(
                id=away_team_model.id,
                name=away_team_model.name,
                logo_url=away_team_model.logo_url,
            )

    return MatchListRead(
        id=match.id,
        api_fixture_id=match.api_fixture_id,
        match_date=match.match_date,
        status_long=match.status_long,
        status_short=match.status_short,
        elapsed=match.elapsed,
        home_goals=match.home_goals,
        away_goals=match.away_goals,
        venue_name=match.venue_name,
        venue_city=match.venue_city,
        league=league,
        home_team=home_team,
        away_team=away_team,
    )