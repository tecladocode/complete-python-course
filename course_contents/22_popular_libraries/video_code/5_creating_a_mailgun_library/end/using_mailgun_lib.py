from libs.mailgun import Mailgun

Mailgun.send_email(['test@gmail.com'],
                   subject='Test e-mail',
                   content='This is a test e-mail')
