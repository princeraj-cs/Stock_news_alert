# Stock News Alert 📈📰

A Python script that tracks Tesla stock price movement and sends top related news headlines by SMS when the daily change is significant.

## What this project does 🚀

- Fetches recent TSLA closing prices using Yahoo Finance 📊
- Calculates percentage change between the last two trading days 🧮
- If the absolute change is greater than 2%, fetches recent Tesla news 🗞️
- Sends up to 3 headlines via Twilio SMS 📱

## Tech stack 🛠️

- Python 3.x
- `requests`
- `yfinance`
- `twilio`

## Setup ⚙️

1. Clone or download this project.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

```bash
pip install requests yfinance twilio
```

## Configuration 🔐

Update the following variables in `main.py`:

- `NEWS_API`: Your NewsAPI key
- `TWILIO_SID`: Your Twilio Account SID
- `AUTH_TOKEN`: Your Twilio Auth Token
- `from_`: Your Twilio phone number
- `to`: Your destination phone number

You can also change:

- `STOCK_NAME` (default: TSLA)
- `COMPANY_NAME` (default: Tesla Inc)

## How to get the NewsAPI key 🔑

1. Go to https://newsapi.org.
2. Click **Get API Key** and create a free account.
3. Verify your email if prompted.
4. Open your account dashboard and copy your API key.
5. Paste that value into `NEWS_API` in `main.py`.

## How to get Twilio SID, Auth Token, and phone numbers ☎️

1. Go to https://www.twilio.com/try-twilio and create an account.
2. Complete email and phone verification.
3. In the Twilio Console dashboard, copy:
   - **Account SID** -> paste into `TWILIO_SID`
   - **Auth Token** -> paste into `AUTH_TOKEN`
4. Get a Twilio number:
   - In Console, go to **Phone Numbers > Manage > Buy a number**
   - Buy/select a number with SMS capability
   - Put this number in the `from_` field
5. Set your destination number in `to` using international E.164 format, for example `+919876543210`.
6. If you are using a Twilio trial account, verify your recipient number in:
   - **Console > Account > API keys & tokens / Verified Caller IDs**
   - Twilio may block SMS to unverified numbers on trial plans.

## Run ▶️

```bash
python main.py
```

## Notes 📝

- This script uses a threshold of 2% price movement 📉📈
- News is fetched using `qInTitle` with the company name 🧠
- Keep API keys and tokens private. For production, use environment variables instead of hardcoding secrets 🔒

## File structure 📂

- `main.py`: Core script logic
- `README.md`: Project documentation
