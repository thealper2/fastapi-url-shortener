"""
Service functions for the URL Shortener application.

This module contains business logic and utility functions for generating keys
and processing URL-related operations.
"""

import secrets
import string
from typing import Tuple

from config import URL_KEY_LENGTH, SECRET_KEY_LENGTH


def generate_url_key(length: int = URL_KEY_LENGTH) -> str:
    """
    Generate a random URL key with the specified length.

    Args:
        length: The length of the URL key. Defaults to value from config.

    Returns:
        str: A random URL key consisting of letters and digits.

    Example:
        >>> generate_url_key()
        'ab3D9f'
    """
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))


def generate_secret_key(length: int = SECRET_KEY_LENGTH) -> str:
    """
    Generate a random secret key with the specified length.

    Uses a cryptographically secure random generator to create a URL-safe token.

    Args:
        length: The approximate length of the URL key in bytes.
               Defaults to value from config.

    Returns:
        str: A random URL-safe secret key.

    Example:
        >>> generate_secret_key()
        'dZF-LJGMvnQlBDfWsxypTg'
    """
    return secrets.token_urlsafe(length)


def generate_keys() -> Tuple[str, str]:
    """
    Generate both URL key and secret key.

    Returns:
        Tuple[str, str]: A tuple containing (url_key, secret_key).
    """
    return generate_url_key(), generate_secret_key()
