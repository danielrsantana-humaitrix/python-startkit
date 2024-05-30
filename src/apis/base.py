from fastapi import APIRouter
from datetime import datetime
from settings import settings
from interfaces import IBaseMessage

router = APIRouter()


@router.get("/hello-world", response_model=IBaseMessage)
async def get_is_online():
    return {
        "is_online": True,
        "date_time": datetime.now(),
        "message": "🚀 Hello World!",
        "version": settings.SERVER_VERSION,
    }
