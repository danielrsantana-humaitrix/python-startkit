from datetime import datetime
from typing_extensions import TypedDict


class IBaseMessage(TypedDict):
    is_online: bool
    date_time: datetime
    message: str
    version: str
