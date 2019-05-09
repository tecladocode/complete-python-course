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

email = EmailMessage()

email['Subject'] = 'Test email'
email['From'] = 'email@gmail.com'
email['To'] = 'john@gmail.com'

email.set_content('Hello, John')

s = smtplib.SMTP(host='smtp.gmail.com', port=587)
s.starttls()
s.login('you@gmail.com', 'password')

s.send_message(email)
s.quit()
