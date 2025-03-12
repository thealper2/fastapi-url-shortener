"""
Root endpoint routes for the URL Shortener application.
"""

from typing import Dict
from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def root() -> Dict[str, str]:
    """
    Root endpoint - returns a welcome message.

    Returns:
        Dict[str, str]: A dictionary with a welcome message.
    """
    return {"message": "Hello, World!"}
