from requests import get, post, put, delete, patch

headers = {
    "ContentType": "application/json"
}
response = get("https://swapi.dev/api/people/2")
print(response.json())