import datetime

from pathlib import Path

from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from auth.jwt_bearer import JWTBearer
from database.database import status_collection, attendees_collection, conference_collection
from routes.admin import router as admin_router
from routes.healthcheck import router as healthcheck_router
from routes.status import router as status_router
from routes.attendee import router as attendee_router
from routes.conference import router as conference_router
from routes.coference_u import router as conference_router_u


app = FastAPI(
    title="bITconf ♥",
    description="bITconf API will help you during the workshop",
    contact={
        "names": "Michał Bek",
        "profile": "https://www.linkedin.com/in/michal-bek/",
        "email": "michal.bek@gmail.com"
    })


base_path = Path(__file__).resolve().parent
app.mount("/templates/static", StaticFiles(directory="templates/static"), name="static")
templates = Jinja2Templates(directory=str(base_path / "templates"))
token_listener = JWTBearer()


@app.get("/", tags=["Root"])
async def read_root(request: Request):
    return templates.TemplateResponse("/shared/base.html", {"request": request})


@app.route("/start")
async def get_start(request: Request):
    refresh_time = str(datetime.datetime.now().isoformat())[:19].replace("T", " ")
    attendee_list = await attendees_collection.find({}).sort([('_id', 1)]).to_list(length=None)
    conference_list = await conference_collection.find({}).sort([('_id', 1)]).to_list(length=None)
    app_status_list = await status_collection.find({}).sort([('_id', 1)]).to_list(length=None)
    app_status = app_status_list[-1]["status"]
    return templates.TemplateResponse("start/start.html", {"request": request,
                                                           "app_status": app_status,
                                                           "attendees": attendee_list,
                                                           "conferences": conference_list,
                                                           "refresh_time": refresh_time})


app.include_router(admin_router, tags=["Administrator"])
app.include_router(healthcheck_router, tags=["Healthcheck"])
app.include_router(status_router, tags=["Status"], prefix="/status")
app.include_router(attendee_router, tags=["Attendees"], prefix="/attendee", dependencies=[Depends(token_listener)])
app.include_router(conference_router, tags=["Conferences"], prefix="/conference", dependencies=[Depends(token_listener)])
app.include_router(conference_router_u, tags=["Conferences"], prefix="/conference")
