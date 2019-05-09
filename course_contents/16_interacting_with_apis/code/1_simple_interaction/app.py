import requests

APP_ID = "72dba35060b54cf9ad3ffbdc68de9174"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates['rates']['GBP']

print(f"USD{usd_amount} is GBP{gbp_amount}")