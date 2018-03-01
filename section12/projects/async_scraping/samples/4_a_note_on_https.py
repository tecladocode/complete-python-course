"""
Running this file may fail with an error like this one:

----
...
  File "...lib/python3.7/site-packages/aiohttp/connector.py", line 803, in _wrap_create_connection
    req.connection_key, exc) from exc
aiohttp.client_exceptions.ClientConnectorCertificateError: Cannot connect to
host www.johnlewis.com:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED]
certificate verify failed: unable to getlocal issuer certificate (_ssl.c:959)')]

----

If that is the case, you may need to install Python's SSL certificates. In OS X, they don't come installed.

This is because OS X provides deprecated versions of an important library for SSL verification (the technology
that's behind HTTPS) called OpenSSL, so Python3.6 and Python3.7 (and probably future versions too) now ship with their own
version of OpenSSL. This also means that the trust certificates in system and user keychains managed by the Keychain Access
application and the security command line utility are no longer used as defaults by the Python ssl module.

For 3.6.0, a sample command script is included in /Applications/Python 3.6 to install a curated bundle of default root
certificates from the third-party certifi package (https://pypi.python.org/pypi/certifi).
If you choose to use certifi, you should consider subscribing to the project's email update service to be
notified when the certificate bundle is updated.

If you are on OS X, run the file:

- /Applications/Python 3.6/Install Certificates.command

or

- /Applications/Python 3.7/Install Certificates.command
"""

import asyncio
import aiohttp
import async_timeout
import time

async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        loop = asyncio.get_event_loop()
        urls = [
            'http://google.com',
            'http://example.com',
            'https://www.johnlewis.com/herman-miller-new-aeron-office-chair-graphite-polished-aluminium/p3177260'  # this can cause issues on fresh installations of Python3.6 or 3.7 on OS X.
        ]
        start = time.time()
        pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()