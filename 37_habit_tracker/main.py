import requests
from datetime import datetime

TOKEN = "token"
USERNAME = "test123432535"
GRAPH_ID = "graph1"


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params).json()


graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Habit Graph",
    "unit": "time(s)",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers).json()


pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers).json()

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "100",
}

# requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# requests.delete(url=delete_endpoint, headers=headers)
