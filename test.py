import requests

url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "list": "search",
    "srsearch": "India Pakistan geopolitical history",
    "format": "json"
}

headers = {
    "User-Agent": "MyRAGLearningApp/1.0"
}

response = requests.get(
    url,
    params=params,
    headers=headers
)

print(response.status_code)
print(response.text[:500])