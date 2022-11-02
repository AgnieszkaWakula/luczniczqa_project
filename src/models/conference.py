from pydantic import BaseModel, Field


class ConferenceModel(BaseModel):
    name: str = Field(...)
    city: str = Field(...)
    timezone: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "bITconf",
                "city": "Bydgoszcz",
                "timezone": "Europe/Warsaw"
            }
        }


class UpdateConferenceModel(BaseModel):
    name: str = Field(...)
    city: str = Field(...)
    timezone: str = Field(...)

    class Config:
        schema_extra = {
            "hint": "List of timezones can be found here: http://worldtimeapi.org/api/timezone/",
            "example": {
                "name": "PTAQ",
                "city": "Poznan",
                "timezone": "Europe/Warsaw"
            }
        }


def response_model(data, message):
    return {
        "data": data,
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
