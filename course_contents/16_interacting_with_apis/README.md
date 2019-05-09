# Interacting with APIs

## Requirements

- requests
- cachetools (for part 3)
- An account with OpenExchangeRates (free)
  - Generate an **App ID** on their website, you need this to use their API.

## Recap

First two parts recapped here: https://blog.tecladocode.com/how-to-interact-with-apis-using-python/

### Caching

Can use something like `functools.lru_cache` for caching function calls. That is, if you apply this decorator to a function and then you call the function with the same arguments 10 times, 9 of them will be really quick and the function won't evaluate.

Can use `cachetools.TTLCache` to cache a function call for up to a certain amount of time. When interacting with APIs it can be useful as sometimes we won't be interested in repeating the same call over and over.