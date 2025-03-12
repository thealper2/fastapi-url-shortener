"""
Routes package for the URL Shortener application.

This makes the routes directory a package and provides a function to include all routes.
"""

from .root import router as root_router
from .url import router as url_router
from .admin import router as admin_router


def include_routes(app):
    """
    Include all routes in the FastAPI application.

    Args:
        app: The FastAPI application instance.

    Returns:
        None
    """
    app.include_router(root_router)
    app.include_router(url_router)
    app.include_router(admin_router)
