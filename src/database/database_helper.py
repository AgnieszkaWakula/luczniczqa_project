import requests


def admin_helper(admin) -> dict:
    return {
        "id": str(admin["_id"]),
        "username": admin["username"],
        "email": admin["email"],
    }


def status_helper(status) -> dict:
    return {
        "id": str(status["_id"]),
        "status": status["status"]
    }


def attendee_helper(attendee) -> dict:
    return {
        "id": str(attendee["_id"]),
        "fullname": attendee["fullname"],
        "email": attendee["email"],
        "job_description": attendee["job_description"],
        "experience": attendee["experience"],
        "seniority": attendee["seniority"]
    }


def conference_helper(conference) -> dict:
    resp = requests.get(f"http://worldtimeapi.org/api/timezone/{conference['timezone']}")
    current_time = resp.json()["datetime"]

    return {
        "id": str(conference["_id"]),
        "name": conference["name"],
        "city": conference["city"],
        "timezone": conference["timezone"],
        "current_time": current_time
    }
