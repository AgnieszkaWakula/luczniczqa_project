import random
import time

from uuid import uuid4

from fastapi import APIRouter, Body, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from database.database import *
from models.status import *

router = APIRouter()


@router.post("/", response_description="Status data added into the database")
async def add_status_data(response: Response, status_: ApplicationStatus = Body(...)):
    response.headers["X-Egnyte"] = str(uuid4())
    app_status = jsonable_encoder(status_)
    new_status = await add_status(app_status)
    return response_model(new_status, "Status added successfully.")


@router.get("/", response_description="Status retrieved")
async def get_status(response: Response):
    response.headers["X-Egnyte"] = str(uuid4())
    status_ = await retrieve_status()
    if not status_:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empty statuses list.",
            headers={"X-Egnyte": str(uuid4())})
    if random.randint(0, 1):
        return response_model(status_, "Status data retrieved successfully")
    else:
        time.sleep(3)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Some error occurred. Please contact Workshop Organizers!",
            headers={"X-Egnyte": str(uuid4())})