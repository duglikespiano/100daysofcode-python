import requests
import json
from twilio.rest import Client

with open("info.json") as data_file:
    data = json.load(data_file)
    STOCK_API_KEY = data["stock_api_key"]
    NEWS_API_KEY = data["news_api_key"]
    TWILIO_ACCOUNT_SID = data["twilio_account_sid"]
    TWILIO_AUTH_TOKEN = data["twilio_auth_token"]
    TWILIO_PHONE_NUMBER = data["twilio_phone_number"]

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]


day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = float(yesterday_closing_price) - \
    float(day_before_yesterday_closing_price)
up_down = None

if difference > 0:
    up_down = "▲"
else:
    up_down = "▼"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()
    articles = news_response["articles"]
    three_articles = articles[:3]

    formatted_articles = [
        f"{STOCK_NAME } : {up_down}{diff_percent}%\nHeadline : {article['title']}. \n Brief : {article['description']}" for article in three_articles]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            body=article,
            to="+821031137815"
        )
