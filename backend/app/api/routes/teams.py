from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.team import Team
from app.schemas.team import TeamRead


router = APIRouter(
    prefix="/teams",
    tags=["Teams"],
)


@router.get("/", response_model=list[TeamRead])
def list_teams(
    session: Annotated[Session, Depends(get_session)],
):
    statement = select(Team)
    teams = session.exec(statement).all()

    return teams