from libs.openexchange import OpenExchangeClient

APP_ID = "f9cf1e8cc7904d508ea265a276de3b1e"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')

print(f"USD{usd_amount} is GBP{gbp_amount}")