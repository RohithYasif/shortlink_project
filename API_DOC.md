### API Documentation

POST /shorten
Shortens a provided URL.

Request:

Method: POST
URL: /shorten
Body (JSON):
json
Copy code
{
  "url": "http://rohith.com/long-url"
}

Response:

Status: 201 Created
Body (JSON):
json
Copy code
{
  "shortened_url": "http://127.0.0.1:5000/sample-URL"
}
GET /{short_code}
Redirects to the original URL using the provided short code.

Request:

Method: GET
URL: /abc123 (where abc123 is the short code)
Response:

Status: 302 Found (Redirects to the original URL)

Error:

Status: 404 Not Found
Body (JSON):
json
Copy code
{
  "error": "Shortened URL not found"
}