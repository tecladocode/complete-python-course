import requests


MAILGUN_API_URL = 'your_url'
MAILGUN_API_KEY = 'your_api_key'

FROM_NAME = 'Jose'
FROM_EMAIL = 'jose@schoolofcode.me'

TO_EMAILS = ['jslvtr@gmail.com']
SUBJECT = 'Test e-mail'
CONTENT = 'Hello, this is a test e-mail'

requests.post(
    MAILGUN_API_URL,
    auth=('api', MAILGUN_API_KEY),  # This is Basic Auth
    data={
        'from': f'{FROM_NAME} <{FROM_EMAIL}>',
        'to': TO_EMAILS,
        'subject': SUBJECT,
        'text': CONTENT
    })
