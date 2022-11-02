from uuid import uuid4

import motor.motor_asyncio

from bson import ObjectId
from decouple import config
from fastapi import HTTPException, status

from .database_helper import admin_helper, status_helper, attendee_helper, conference_helper

MONGO_DETAILS = config("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.luczniczqa

admin_collection = database.get_collection("admins")
status_collection = database.get_collection("status")
attendees_collection = database.get_collection("attendees_collection")
conference_collection = database.get_collection("conference_collection")


async def add_admin(admin_data: dict) -> dict:
    admin = await admin_collection.insert_one(admin_data)
    new_admin = await admin_collection.find_one({"_id": admin.inserted_id})
    return admin_helper(new_admin)


async def add_status(status_data: dict) -> dict:
    status = await status_collection.insert_one(status_data)
    new_status = await status_collection.find_one({"_id": status.inserted_id})
    return status_helper(new_status)


async def retrieve_status() -> dict:
    statuses = []
    async for status_ in status_collection.find():
        statuses.append(status_helper(status_))
    if not statuses:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empty status list.",
            headers={"X-bITconf": str(uuid4())})
    else:
        return statuses[-1]


async def retrieve_attendees():
    attendees = []
    async for attendee in attendees_collection.find():
        attendees.append(attendee_helper(attendee))
    return attendees


async def add_attendee(attendee_data: dict) -> dict:
    attendee = await attendees_collection.insert_one(attendee_data)
    new_attendee = await attendees_collection.find_one({"_id": attendee.inserted_id})
    return attendee_helper(new_attendee)


async def retrieve_attendee(id: str) -> dict:
    attendee = await attendees_collection.find_one({"_id": ObjectId(id)})
    if attendee:
        return attendee_helper(attendee)


async def delete_attendee(id: str):
    attendee = await attendees_collection.find_one({"_id": ObjectId(id)})
    if attendee:
        await attendees_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_attendee_data(id: str, data: dict):
    attendee = await attendees_collection.find_one({"_id": ObjectId(id)})
    if attendee:
        attendees_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True


async def retrieve_conferences():
    conferences = []
    async for university in conference_collection.find():
        conferences.append(conference_helper(university))
    return conferences


async def add_conferences(conferences_data: dict) -> dict:
    conference = await conference_collection.insert_one(conferences_data)
    new_conference = await conference_collection.find_one({"_id": conference.inserted_id})
    return conference_helper(new_conference)


async def retrieve_conference(id: str) -> dict:
    conference = await conference_collection.find_one({"_id": ObjectId(id)})
    if conference:
        return conference_helper(conference)


async def delete_conference(id: str):
    conference = await conference_collection.find_one({"_id": ObjectId(id)})
    if conference:
        await conference_collection.delete_one({"_id": ObjectId(id)})
        return True


async def update_conference_data(id: str, data: dict):
    conference = await conference_collection.find_one({"_id": ObjectId(id)})
    if conference:
        conference_collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        return True
