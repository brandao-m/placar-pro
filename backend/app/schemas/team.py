from typing import Optional

from sqlmodel import SQLModel

class TeamRead(SQLModel): 
    id: int
    api_team_id: int
    name: str
    country: Optional[str] = None
    logo_url: Optional[str] = None
    season: Optional[int] = None