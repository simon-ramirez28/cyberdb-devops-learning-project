from datetime import datetime, timezone

from pydantic import BaseModel, Field


class DataCreate(BaseModel):
    content: str = Field(..., min_length=1, description="Contenido del dato")
    source: str | None = Field(None, description="Corporación o fuente de origen")


class DataResponse(BaseModel):
    id: str
    handle: str
    content: str
    source: str | None
    hash: str
    created_at: datetime


class Stats(BaseModel):
    total: int
    top_handles: list[dict]
    recent: list[DataResponse]
