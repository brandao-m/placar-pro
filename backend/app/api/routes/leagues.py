from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.league import League
from app.schemas.league import LeagueRead


router = APIRouter(
    prefix='/leagues',
    tags=['Leagues'],
)


@router.get('/', response_model=list[LeagueRead])
def list_leagues(
    session: Annotated[Session, Depends(get_session)],
):
    statement = select(League)
    leagues = session.exec(statement).all()

    return leagues