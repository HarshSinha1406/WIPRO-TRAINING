import requests

patchurl = "https://api.restful-api.dev/objects/7"

response = requests.get(patchurl)

print("get status code", response.status_code)
print(response.json())

patchurl = "https://api.restful-api.dev/objects/7"

body1 ={
   "name": "Apple MacBook Pro 16 (Updated Name)"
}

r1 = requests.patch(patchurl, json=body1);
print("patch status code", r1.status_code)
print(r1.json())
