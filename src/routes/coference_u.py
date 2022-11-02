from uuid import uuid4

from fastapi import APIRouter, Body, Response, HTTPException, status

from database.database import *
from models.conference import *

router = APIRouter()


# unsecured
@router.get("/{id}", response_description="Conference data retrieved")
async def get_conference_data(id, response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    conference = await retrieve_conference(id)
    if not conference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conference with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model(conference, "Conference data retrieved successfully")
