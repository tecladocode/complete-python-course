import requests

APP_ID = "c640347fae594fc5add36046c807b282"
ENDPOINT = "https://openexchangerates.org/api/latest.json"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
exchange_rates = response.json()

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["rates"]["GBP"]

print(f"USD{usd_amount} is GBP{gbp_amount}")
