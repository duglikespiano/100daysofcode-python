import json
import requests
from datetime import datetime


with open("info.json") as data_file:
    data = json.load(data_file)
    GENDER = data["GENDER"]
    WEIGHT_KG = data["WEIGHT_KG"]
    HEIGHT_CM = data["HEIGHT_CM"]
    AGE = data["AGE"]
    NUTRITIONIX_APP_ID = data["NUTRITIONIX_APP_ID"]
    NUTRITIONIX_API_KEY = data["NUTRITIONIX_API_KEY"]
    SHEETY_SHEET_ENDPOINT = data["SHEETY_SHEET_ENDPOINT"]
    SHEETY_BEARER_TOKEN = data["SHEETY_BEARER_TOKEN"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
    }

    sheet_response = requests.post(
        SHEETY_SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
