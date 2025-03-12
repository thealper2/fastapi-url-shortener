"""
URL creation and redirection routes for the URL Shortener application.
"""

from typing import Dict, Any
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import RedirectResponse

from models import URLCreate, URL
from dependencies import get_url_by_url_key
from database import create_url_in_db, increment_clicks
from services import generate_keys

router = APIRouter()


@router.post("/url", response_model=URL, status_code=status.HTTP_201_CREATED)
async def create_url(url: URLCreate) -> Dict[str, Any]:
    """
    Create a shortened URL from a target URL.

    Args:
        url: The URLCreate model containing the target URL.

    Returns:
        Dict[str, Any]: A dictionary containing the created URL data.

    Raises:
        HTTPException: 400 error if there's a URL key collision.
    """
    # Generate keys
    url_key, secret_key = generate_keys()

    try:
        # Save to database
        url_data = create_url_in_db(url_key, str(url.target_url), secret_key)
        return url_data
    except Exception as e:
        # Handle potential database errors
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Failed to create shortened URL: {str(e)}",
        )


@router.get("/{url_key}")
async def forward_to_target_url(
    url_data: Dict[str, Any] = Depends(get_url_by_url_key),
) -> RedirectResponse:
    """
    Forward to the target URL and increment click counter.

    Args:
        url_data: URL data retrieved from the database by url_key.

    Returns:
        RedirectResponse: Redirect response to the target URL.
    """
    # Update click count
    increment_clicks(url_data["url_key"])

    # Redirect to target URL
    return RedirectResponse(url=url_data["target_url"])
