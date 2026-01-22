import requests

url = "https://api.restful-api.dev/objects"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response:")
print(response.json())
