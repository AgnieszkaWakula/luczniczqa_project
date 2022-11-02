from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class AttendeeModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    job_description: str = Field(...)
    experience: int = Field(...)
    seniority: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Miszka Kiszka",
                "email": "mkiszka@example.com",
                "job_description": "I can test potato!",
                "experience": 2,
                "seniority": "extreme junior"
            }
        }


class UpdateAttendeeModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    job_description: Optional[str]
    experience: Optional[int]
    seniority: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Miszka Kiszka",
                "email": "kiszkam@example.org",
                "job_description": "Water resources and environmental engineering",
                "experience": 4,
                "seniority": "even moe extreme junior"
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
