from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class League(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    api_league_id: int = Field(index=True, unique=True)
    name: str
    country: Optional[str] = None
    logo_url: Optional[str] = None
    season: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
