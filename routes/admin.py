"""
Admin routes for the URL Shortener application.
"""

from typing import Dict, Any
from fastapi import APIRouter, Depends, status

from models import URLInfo
from dependencies import get_url_by_admin_key
from database import deactivate_url

router = APIRouter()


@router.get("/admin/{secret_key}", response_model=URLInfo)
async def get_url_info(
    url_data: Dict[str, Any] = Depends(get_url_by_admin_key),
) -> Dict[str, Any]:
    """
    Get administrative information about a shortened URL.

    Args:
        url_data: URL data retrieved from the database by secret key.

    Returns:
        Dict[str, Any]: A dictionary containing URL information.
    """
    return url_data


@router.delete("/admin/{secret_key}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_url(url_data: Dict[str, Any] = Depends(get_url_by_admin_key)) -> None:
    """
    Delete a shortened URL (mark as inactive).

    Args:
        url_data: URL data retrieved from the database by secret key.

    Returns:
        None
    """
    deactivate_url(url_data["secret_key"])
    return None
