from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException
from .base import router as base_router

apis = APIRouter()
apis.include_router(base_router)
