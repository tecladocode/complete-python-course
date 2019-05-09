"""
To send e-mails via Mailgun, you first need to create an account:

https://signup.mailgun.com/new/signup

Create a "Pay As You Go" account to get 100,000 free e-mails every month.
For learning, you won't need any more than this!

Once you've created your account, you can send e-mails to yourself using
the sandbox account and API key.

If you want to send e-mails from an address that uses your domain, you must
link your domain name with Mailgun (something outside the scope of this course).
"""

import requests

MAILGUN_DOMAIN = ''
MAILGUN_API_KEY = ''
FROM_NAME = ''
FROM_EMAIL = ''

TO_EMAILS = ['test@email.com']
SUBJECT = 'Test e-mail'
CONTENT = 'Hello, this is a test e-mail.'

requests.post(
    "https://api.mailgun.net/v3/{}/messages".format(MAILGUN_DOMAIN),
    auth=("api", MAILGUN_API_KEY),
    data={
        "from": "{} <{}>".format(FROM_NAME, FROM_EMAIL),
        "to": TO_EMAILS,
        "subject": SUBJECT,
        "text": CONTENT
    })
