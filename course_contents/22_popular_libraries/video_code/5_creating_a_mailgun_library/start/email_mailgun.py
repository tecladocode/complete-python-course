import requests


MAILGUN_API_URL = 'https://api.mailgun.net/v3/sandbox0fd1d065f521484b8af277034648e756.mailgun.org'
MAILGUN_API_KEY = 'key-798b9585aedd35d87f1bf506cadc221e'

FROM_NAME = 'Jose'
FROM_EMAIL = 'jose@schoolofcode.me'

TO_EMAILS = ['jslvtr@gmail.com']
SUBJECT = 'Test e-mail'
CONTENT = 'Hello, this is a test e-mail'

print(requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),  # This is Basic Auth
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    }))
