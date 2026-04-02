import requests
import yfinance as yf
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API = "ADD_YOUR API" # Stock news api- https://newsapi.org/docs

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "YOUR_SID" #twilio link for SID & Token- https://www.twilio.com/en-us
AUTH_TOKEN = "YOUR_TOKEN"

stock = yf.Ticker("TSLA")
data = stock.history(period="3d")

# Get closing prices
yesterday_close = data["Close"].iloc[-1]
print(yesterday_close)
day_before_close = data["Close"].iloc[-2]
print(day_before_close)

# Calculate percentage
price_diff = yesterday_close - day_before_close

up_down = None
if price_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage = (price_diff / day_before_close) * 100

print("Percentage Change:", percentage)


news_params = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME,
    "language": "en",
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_data = news_response.json()

if abs(percentage) > 2:
    news_articles = news_data["articles"]
    three_articles = news_articles[0:3]
    
    article_list = [f"Headline: {article['title']}"for article in three_articles]

    client = Client(TWILIO_SID, AUTH_TOKEN)
    for article in article_list:
        message = client.messages.create(
            body=f"{STOCK_NAME}: 2% {up_down} \n{article}",
            from_="YOUR_TWILIO_NO",
            to="YOUR_NO",
        )
        print(message.body)

