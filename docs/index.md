# URL Shortener Documentation

A modern URL shortening service built with FastAPI and SQLite.

## Features

- Easy URL shortening
- Secure management keys
- Tracking statistics
- RESTful API

## Quick Start

```python
# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

You can access the API at [http://localhost:8000/docs](http://localhost:8000/docs).

## API Endpoints

| Endpoint | Method | Description |
|----------|-------|----------|
| `/` | GET | Returns a welcome message |
| `/url` | POST | Creates a new short URL |
| `/{url_key}` | GET | Redirects to target URL |
| `/admin/{secret_key}` | GET | Shows information about the URL |
| `/admin/{secret_key}` | DELETE | Disables the URL |

For more detailed information, see [API Usage](guide/api-usage.md).