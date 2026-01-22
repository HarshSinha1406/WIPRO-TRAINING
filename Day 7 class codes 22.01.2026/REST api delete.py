import requests

deleteurl = "https://api.restful-api.dev/objects/6"

response = requests.get(deleteurl)
print("get status code", response.status_code)
print(response.json())

r1 = requests.delete(deleteurl)

print("delete status code", r1.status_code)


if r1.text:
    print(r1.json())
else:
    print("Object deleted successfully")

