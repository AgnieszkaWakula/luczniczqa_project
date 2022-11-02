import logging

from uuid import uuid4

from fastapi import APIRouter, Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.conference import *

router = APIRouter()
logger = logging.getLogger("api")


@router.get("/", response_description="Attendees retrieved")
async def get_conferences(response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    conferences = await retrieve_conferences()
    if not conferences:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Empty conferences list.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model(conferences, "Conferences data retrieved successfully")


# @router.get("/{id}", response_description="Conference data retrieved")
# async def get_conference_data(id, response: Response):
#     response.headers["X-bITconf"] = str(uuid4())
#     conference = await retrieve_conference(id)
#     if not conference:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"Conference with {id} doesn't exist.",
#             headers={"X-bITconf": str(uuid4())})
#     else:
#         return response_model(conference, "Conference data retrieved successfully")


@router.post("/", response_description="Conference data added into the database")
async def add_conference_data(response: Response, conference: ConferenceModel = Body(...)):
    response.headers["X-bITconf"] = str(uuid4())
    conference = jsonable_encoder(conference)
    new_conference = await add_conferences(conference)
    logger.debug(response_model(new_conference, "This is test"))
    return response_model(new_conference, "Conference added successfully.")


@router.delete("/{id}", response_description="Conference data deleted from the database")
async def delete_conference_data(id: str, response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    deleted_conference = await delete_conference(id)
    if not deleted_conference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conference with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model("Conference with ID: {} removed".format(id), "Conference deleted successfully")


@router.put("/{id}")
async def update_conference(id: str, response: Response, req: UpdateConferenceModel = Body(...)):
    response.headers["X-bITconf"] = str(uuid4())
    updated_conference = await update_conference_data(id, req.dict())
    if not updated_conference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Conference with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model("Conference with ID: {} data update is successful".format(id),
                              "Conference data updated successfully")
