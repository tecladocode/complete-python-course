import time
from libs.openexchange import OpenExchangeClient
APP_ID = "f9cf1e8cc7904d508ea265a276de3b1e"

client = OpenExchangeClient(APP_ID)
usd_amount = 1000
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)
start = time.time()
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()
print(end - start)

print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
