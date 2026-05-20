from fastapi import APIRouter, HTTPException, Query

from app.database import create, delete, get_all, get_by_id
from app.models import DataCreate, DataResponse

router = APIRouter(prefix="/api/data", tags=["data"])


@router.post("", response_model=DataResponse, status_code=201)
def create_data(payload: DataCreate):
    return create(payload)


@router.get("", response_model=list[DataResponse])
def list_data(skip: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=100)):
    return get_all(skip=skip, limit=limit)


@router.get("/{record_id}", response_model=DataResponse)
def get_data(record_id: str):
    record = get_by_id(record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Data not found")
    return record


@router.delete("/{record_id}", status_code=204)
def delete_data(record_id: str):
    if not delete(record_id):
        raise HTTPException(status_code=404, detail="Data not found")
