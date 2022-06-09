from datetime import datetime, timezone, timedelta

print(datetime.now())

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)
print(tomorrow)

print(today.strftime('%d-%m-%Y %H:%M:%S'))

user_date = input('Enter the date in YYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)
