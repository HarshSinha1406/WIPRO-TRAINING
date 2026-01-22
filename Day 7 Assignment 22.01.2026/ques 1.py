import requests
import json

url = "https://jsonplaceholder.typicode.com/users"  # Public REST API

headers = {
    "User-Agent": "Python-Requests/1.0",
    "Accept": "application/json"
}

try:
    response = requests.get(url, headers=headers)

    response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)

    data = response.json()

    extracted_data = []
    for user in data:
        user_info = {
            "id": user.get("id"),
            "name": user.get("name"),
            "username": user.get("username"),
            "email": user.get("email")
        }
        extracted_data.append(user_info)

    with open("users_data.json", "w") as json_file:
        json.dump(extracted_data, json_file, indent=4)

    print("Data extracted and saved to users_data.json successfully!")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as e:
    print(f"An error occurred: {e}")
