"""
FastAPI dependency functions for the URL Shortener application.

This module contains reusable dependencies for route handlers.
"""

from typing import Dict, Any

from fastapi import HTTPException, status

from database import get_url_by_key, get_url_by_secret_key


def get_url_by_url_key(url_key: str) -> Dict[str, Any]:
    """
    Dependency for retrieving URL by URL key.

    Args:
        url_key: The short URL key to look up.

    Returns:
        Dict[str, Any]: A dictionary containing URL data.

    Raises:
        HTTPException: 404 error if URL not found or inactive.
    """
    try:
        return get_url_by_key(url_key)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="URL not found or inactive"
        )


def get_url_by_admin_key(secret_key: str) -> Dict[str, Any]:
    """
    Dependency for retrieving URL by secret key.

    Args:
        secret_key: The secret key to look up.

    Returns:
        Dict[str, Any]: A dictionary containing URL data.

    Raises:
        HTTPException: 404 error if URL not found.
    """
    try:
        return get_url_by_secret_key(secret_key)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="URL not found for this secret key",
        )
