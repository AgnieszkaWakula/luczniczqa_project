from uuid import uuid4

from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from passlib.context import CryptContext

from database.database import admin_collection

security = HTTPBasic()
hash_helper = CryptContext(schemes=["bcrypt"])


async def validate_login(credentials: HTTPBasicCredentials = Depends(security)):
    admin = admin_collection.find_one({"username": credentials.username})
    if admin:
        password = hash_helper.verify(credentials.password, admin["password"])
        if not password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"X-bITconf": str(uuid4())}
            )
        return True
    return False
