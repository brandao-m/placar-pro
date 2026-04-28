from typing import Optional 

from sqlmodel import SQLModel


class LeagueRead(SQLModel):
    id: int
    api_league_id: int 
    name: str
    country: Optional[str] = None
    logo_url: Optional[str] = None
    season: Optional[int] = None