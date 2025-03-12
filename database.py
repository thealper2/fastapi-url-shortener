"""
Database utilities for the URL Shortener application.

This module contains functions for database connection, initialization
and common database operations.
"""

import sqlite3
from contextlib import contextmanager
from typing import Generator, Dict, Any

from config import DATABASE_NAME


@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """
    Context manager for database connection.

    Creates a new SQLite connection for each request, ensuring proper
    resource management and connection closing.

    Yields:
        sqlite3.Connection: A SQLite database connection with row factory set.
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()


def init_db() -> None:
    """
    Initialize the database with required tables.

    Creates the 'urls' table if it doesn't exist yet with all necessary
    columns and constraints.

    Returns:
        None

    Raises:
        sqlite3.Error: If there's an issue with database initialization.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY,
            url_key TEXT UNIQUE NOT NULL,
            target_url TEXT NOT NULL,
            secret_key TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            is_active BOOLEAN DEFAULT TRUE,
            clicks INTEGER DEFAULT 0
        );
        """)
        conn.commit()


def get_url_by_key(url_key: str) -> Dict[str, Any]:
    """
    Retrieve URL data from the database by URL key.

    Args:
        url_key: The short URL key to look up.

    Returns:
        Dict[str, Any]: A dictionary containing all URL data fields.

    Raises:
        ValueError: If the URL with the given key is not found or not active.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM urls WHERE url_key = ? AND is_active = TRUE", (url_key,)
        )
        url_data = cursor.fetchone()

    if url_data is None:
        raise ValueError(f"URL with key '{url_key}' not found or inactive.")

    return dict(url_data)


def get_url_by_secret_key(secret_key: str) -> Dict[str, Any]:
    """
    Retrieve URL data from the database by secret key.

    Args:
        secret_key: The secret key to look up.

    Returns:
        Dict[str, Any]: A dictionary containing all URL data fields.

    Raises:
        ValueError: If the URL with the given secret key is not found.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM urls WHERE secret_key = ?", (secret_key,))
        url_data = cursor.fetchone()

    if url_data is None:
        raise ValueError(f"URL with {secret_key} not found.")

    return dict(url_data)


def create_url_in_db(url_key: str, target_url: str, secret_key: str) -> Dict[str, Any]:
    """
    Create a new shortened URL in the database.

    Args:
        url_key: The generated short URL key.
        target_url: The original URL to be shortened.
        secret_key: The generated secret key for admin operations.

    Returns:
        Dict[str, Any]: The created URL data as a dictionary.

    Raises:
        sqlite3.IntegrityError: If there's a key collision.
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO urls (url_key, target_url, secret_key, created_at)
            VALUES (?, ?, ?, datetime('now'))
            """,
            (url_key, target_url, secret_key),
        )
        conn.commit()

    # Get the created URL data
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM urls WHERE url_key = ?", (url_key,))
        url_data = dict(cursor.fetchone())

    return url_data


def increment_clicks(url_key: str) -> None:
    """
    Increment the click counter for a given URL.

    Args:
        url_key: The short URL key.

    Returns:
        None
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE url_key = ?", (url_key,)
        )
        conn.commit()


def deactivate_url(secret_key: str) -> None:
    """
    Mark a URL as inactive (soft delete).

    Args:
        secret_key: The secret key for the URL.

    Returns:
        None
    """
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE urls SET is_active = FALSE WHERE secret_key = ?", (secret_key,)
        )
        conn.commit()
