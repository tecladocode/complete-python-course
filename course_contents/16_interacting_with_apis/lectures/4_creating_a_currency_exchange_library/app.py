from libs.openexchange import OpenExchangeClient

APP_ID = "72dba35060b54cf9ad3ffbdc68de9174"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f"USD{usd_amount} is GBP{gbp_amount}")