# API Usage

## URL Shortening

To shorten a URL, send a POST request to the `/url` endpoint:

```bash
curl -X 'POST' \
  'http://localhost:8000/url' \
  -H 'Content-Type: application/json' \
  -d '{
  "target_url": "https://example.com/very/long/url/that/needs/shortening"
}'
```

Answer:

```json
{
  "target_url": "https://example.com/very/long/url/that/needs/shortening",
  "url_key": "ab3D9f",
  "secret_key": "dZF-LJGMvnQlBDfWsxypTg",
  "created_at": "2023-06-15T10:15:30",
  "is_active": true,
  "clicks": 0
}
```

## URL Redirection

To use the generated URL, go to `http://localhost:8000/{url_key}` in your browser.

## Viewing URL Information

To get information about the URL, use the admin endpoint:

```bash
curl -X 'GET' 'http://localhost:8000/admin/{secret_key}'
```

## Delete URL

To disable the URL:

```bash
curl -X 'DELETE' 'http://localhost:8000/admin/{secret_key}'
```