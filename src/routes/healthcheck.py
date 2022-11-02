import aiohttp
import datetime

from dataclasses import dataclass
from uuid import uuid4

from fastapi import APIRouter, status, Response


router = APIRouter()


@dataclass
class HealthcheckStatistics:

    current_date: str
    bITconf_online: bool


async def get_healthcheck():
    url = "http://127.0.0.1:8080/"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return await response.json(), response.status
        except Exception as ex:
            message = {"error": str(ex)}
            return message, status.HTTP_503_SERVICE_UNAVAILABLE


async def is_bITconf_online():
    message, status_code = await get_healthcheck()
    return True if message["message"] == "Welcome to bITconf API Testing app." else False


@router.get("/healthcheck")
async def get_health(response: Response):
    response.headers["X-bITconf"] = str(uuid4())
    bITconf_status = await is_bITconf_online()
    current_date = datetime.datetime.now()
    healthcheck_statistics = HealthcheckStatistics(current_date=current_date.isoformat(),
                                                   bITconf_online=bITconf_status)
    return healthcheck_statistics
