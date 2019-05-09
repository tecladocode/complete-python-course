"""
If you get an SMTPAuthenticationError even when your password is correct,
it's possible that you have 2-factor authentication enabled.
You'll need to use an App Password to log in instead of your normal password.

If you don't have 2-FA enabled, you'll have to allow access by
less secure apps in your Gmail security preferences—though remember to deactivate
it once you've finished learning about sending e-mails with Python!
"""

import smtplib
from email.message import EmailMessage

email_content = '''Dear Sir/Madam,

I am sending you an e-mail with Python. I hope you like it.

Kind regards,
Jose
'''

email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'you@gmail.com'
email['To'] = 'someonelse@gmail.com'

email.set_content(email_content)


smtp_connector = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtp_connector.starttls()
smtp_connector.login('you@gmail.com', 'password')

smtp_connector.send_message(email)
smtp_connector.quit()
