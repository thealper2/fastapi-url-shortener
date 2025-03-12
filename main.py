"""
Main application file for the URL Shortener.

This module initializes the FastAPI application, database, and includes all routes.
"""

import uvicorn
from fastapi import FastAPI

from database import init_db
from routes import include_routes


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI application instance.
    """
    app = FastAPI(
        title="URL Shortener API",
        description="A simple URL shortener service with SQLite backend",
        version="1.0.0",
    )

    # Include all routes
    include_routes(app)

    return app


app = create_application()


@app.on_event("startup")
async def startup_event() -> None:
    """
    Initialize the database on application startup.

    Returns:
        None
    """
    init_db()


if __name__ == "__main__":
    """
    Run the application directly when executed as a script.
    
    For development use only. In production, use a proper ASGI server.
    """
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
