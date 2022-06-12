from libs.openexchange import OpenExchangeClient
import time



APP_ID = "f9cf1e8cc7904d508ea265a276de3b1e"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'First call took {time.time() - start} seconds.')

start = time.time()
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
gbp_amount = client.convert(usd_amount, 'USD', 'GBP')
print(f'After, 10 calls took {time.time() - start} seconds.')

print(f"USD{usd_amount} is GBP{gbp_amount}")