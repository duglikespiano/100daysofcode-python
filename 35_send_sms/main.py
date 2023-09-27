from twilio.rest import Client
import os
import requests

OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = ""
PHONE_NUMBER = ""

WEATHER_PARAMS = {
    "lat": 0,
    "lon": 0,
    "appid": API_KEY,
    "exclude": "current, minutely, daily"
}

will_rain = False

response = requests.get(OMW_ENDPOINT, params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            from_='',
            body='Ahoy! This message was sent from my Twilio phone number!',
            to='+'
        )
    print(message.status)
