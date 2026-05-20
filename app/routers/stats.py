from fastapi import APIRouter

from app.database import get_stats

router = APIRouter(prefix="/api", tags=["stats"])


@router.get("/stats")
def stats():
    return get_stats()
