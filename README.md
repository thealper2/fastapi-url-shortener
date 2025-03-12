# FastAPI URL Shortener

A simple URL shortener service built with FastAPI and SQLite. This API allows you to shorten long URLs, track the number of clicks, and manage shortened URLs using a secret key.

---

## Features

- **Shorten URLs**: Convert long URLs into short, easy-to-share links.
- **Track Clicks**: Automatically track the number of times a shortened URL is accessed.
- **Admin Management**: Use a secret key to view URL details or deactivate a shortened URL.
- **Database Integration**: Uses SQLite for storing URL data.

## Installation

Clone the repository:

```bash
git clone https://github.com/thealper2/fastapi-url-shortener.git
cd fastapi-url-shortener
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlite3
```

Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000.

##  API Endpoints

### 1. Root Endpoint

- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.
- **Response**:

```json
{
  "message": "Hello, World!"
}
```

### 2. Create Short URL

- **URL**: `/url`
- **Method**: `POST`
- **Description**: Creates a shortened URL from a target URL.
- **Request Body**:

```json
{
  "target_url": "https://example.com"
}
```

- **Response**:

```json
{
  "target_url": "https://example.com",
  "url_key": "abc123",
  "secret_key": "xyz456",
  "created_at": "2023-10-01T12:00:00",
  "is_active": true,
  "clicks": 0
}
```

### 3. Redirect to Target URL

- **URL**: `/{url_key}` 
- **Method**: `GET`
- **Description**: Redirects to the target URL associated with the url_key and increments the click count.
- **Response**: Redirects to the target URL.

### 4. Get URL Information

- **URL**: `/admin/{secret_key}`
- **Method**: `GET`
- **Description**: Retrieves administrative information about a shortened URL using the secret_key.
- **Response**:

```json
{
  "target_url": "https://example.com",
  "url_key": "abc123",
  "created_at": "2023-10-01T12:00:00",
  "is_active": true,
  "clicks": 5
}
```

### 5. Delete Short URL

- **URL**: `/admin/{secret_key}`
- **Method**: `DELETE`
- **Description**: Deactivates a shortened URL using the secret_key.
- **Response**: No content (204).

## Database Schema

The SQLite database contains a single table named urls with the following structure:

```sql
Copy
CREATE TABLE urls (
    id INTEGER PRIMARY KEY,
    url_key TEXT UNIQUE NOT NULL,
    target_url TEXT NOT NULL,
    secret_key TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    clicks INTEGER DEFAULT 0
);
```

## Key Generation

URL Key: A random string of 6 characters (letters and digits).
Secret Key: A random URL-safe string of 16 characters.

## Error Handling

- **404 Not Found**: Returned when a URL key or secret key is not found.
- **400 Bad Request**: Returned in case of a URL key collision (extremely rare).

## License

This project is licensed under the MIT License. See the LICENSE file for details.