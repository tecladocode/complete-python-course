import requests

class Mailgun:
    MAILGUN_API_URL = 'your_url'
    MAILGUN_API_KEY = 'your_api_key'

    FROM_NAME = 'Jose'
    FROM_EMAIL = 'jose@schoolofcode.me'

    @classmethod
    def send_email(cls, to_emails, subject, content):
        requests.post(
            cls.MAILGUN_API_URL,
            auth=('api', cls.MAILGUN_API_KEY),
            data={
                'from': f'{cls.FROM_NAME} <{cls.FROM_EMAIL}>',
                'to': to_emails,
                'subject': subject,
                'text': content
            })
