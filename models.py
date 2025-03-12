"""
Pydantic models for the URL Shortener application.

This module defines the data models for request validation, response formatting
and internal data handling.
"""

from datetime import datetime
from pydantic import BaseModel, HttpUrl, Field


class URLBase(BaseModel):
    """
    Base model for URL-related data.

    Attributes:
        target_url: The original URL to be shortened.
    """

    target_url: HttpUrl = Field(..., description="The original URL to be shortened")


class URLCreate(URLBase):
    """
    Model for URL creation request.

    Inherits all attributes from URLBase.
    """

    pass


class URL(URLBase):
    """
    Model for URL response.

    Attributes:
        url_key: Short URL key.
        secret_key: Secret key for admin operations.
        created_at: Creation timestamp.
        is_active: Whether the URL is active.
        clicks: Number of clicks.
    """

    url_key: str = Field(..., description="Short URL key")
    secret_key: str = Field(..., description="Secret key for admin operations")
    created_at: str = Field(..., description="Creation timestamp")
    is_active: bool = Field(..., description="Whether the URL is active")
    clicks: int = Field(..., description="Number of clicks")

    class Config:
        orm_mode = True


class URLInfo(URLBase):
    """
    Model for URL administrative information.

    Attributes:
        url_key: Short URL key.
        created_at: Creation timestamp.
        is_active: Whether the URL is active.
        clicks: Number of clicks.
    """

    url_key: str
    created_at: datetime
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True
