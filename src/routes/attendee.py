from uuid import uuid4

from fastapi import APIRouter, Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.attendee import *

router = APIRouter()


@router.get("/", response_description="Attendees retrieved")
async def get_attendees(response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    attendees = await retrieve_attendees()
    if not attendees:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empty attendees list.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model(attendees, "Attendees data retrieved successfully")


@router.get("/{id}", response_description="Attendee data retrieved")
async def get_attendee_data(id, response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    attendee = await retrieve_attendee(id)
    if not attendee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendee with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model(attendee, "Attendee data retrieved successfully")


@router.post("/", response_description="Attendee data added into the database")
async def add_attendee_data(response: Response, attendee: AttendeeModel = Body(...)):
    response.headers["X-bITconf"] = str(uuid4())
    attendee = jsonable_encoder(attendee)
    new_attendee = await add_attendee(attendee)
    return response_model(new_attendee, "Attendee added successfully.")


@router.delete("/{id}", response_description="Attendee data deleted from the database")
async def delete_attendee_data(id: str, response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    deleted_attendee = await delete_attendee(id)
    if not deleted_attendee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendee with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model("Attendee with ID: {} removed".format(id), "Attendee deleted successfully")


@router.put("/{id}")
async def update_attendee(id: str, response: Response, req: UpdateAttendeeModel = Body(...)):
    response.headers["X-bITconf"] = str(uuid4())
    updated_attendee = await update_attendee_data(id, req.dict())
    if not updated_attendee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Attendee with {id} doesn't exist.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return response_model("Attendee with ID: {} update is successful".format(id),
                              "Attendee updated successfully")
