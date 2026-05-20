from datetime import datetime, timezone
from uuid import uuid4

from app.models import DataCreate, DataResponse
from app.utils import compute_hash, generate_handle

_store: dict[str, DataResponse] = {}


def create(data: DataCreate) -> DataResponse:
    record = DataResponse(
        id=str(uuid4()),
        handle=generate_handle(),
        content=data.content,
        source=data.source,
        hash=compute_hash(data.content),
        created_at=datetime.now(timezone.utc),
    )
    _store[record.id] = record
    return record


def get_all(skip: int = 0, limit: int = 50) -> list[DataResponse]:
    return list(_store.values())[skip : skip + limit]


def get_by_id(record_id: str) -> DataResponse | None:
    return _store.get(record_id)


def delete(record_id: str) -> bool:
    return _store.pop(record_id, None) is not None


def get_stats() -> dict:
    records = list(_store.values())
    if not records:
        return {"total": 0, "top_handles": [], "recent": []}

    handle_counts: dict[str, int] = {}
    for r in records:
        handle_counts[r.handle] = handle_counts.get(r.handle, 0) + 1

    top = sorted(handle_counts.items(), key=lambda x: -x[1])[:5]
    recent = sorted(records, key=lambda r: r.created_at, reverse=True)[:5]

    return {
        "total": len(records),
        "top_handles": [{"handle": h, "count": c} for h, c in top],
        "recent": recent,
    }
