from typing import Annotated

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.core.database import get_session
from app.models.match import Match
from app.schemas.match import MatchRead


router = APIRouter(
    prefix="/matches",
    tags=["Matches"],
)


@router.get("/", response_model=list[MatchRead])
def list_matches(
    session: Annotated[Session, Depends(get_session)],
):
    statement = select(Match)
    matches = session.exec(statement).all()

    return matches