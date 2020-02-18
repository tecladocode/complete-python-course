"""
Working with dates and times is an extremely useful skill, and it can sometimes be a bit confusing. In this video we look at simplifying working with dates and times slightly using Python built-in modules.

The main date and time module in python is called `datetime`, and confusingly enough the main class in that module is also called `datetime`.
"""

from datetime import datetime

print(datetime.now())

"""
(Watch presentation about timezones if you haven’t already.)
"""

from datetime import datetime, timezone

print(datetime.now(timezone.utc))

"""
Normally I would recommend always working with UTC times—store UTC in your database and work with UTC in your code.

When a user gives you a time, convert it to UTC.

When you show the user a time, convert it to their timezone.

That way, you only have to deal with timezones when you show a time to a user; and you don’t have to work with timezones at any other point in your system.

You can add or subtract times:
"""

from datetime import datetime, timedelta

today = datetime.now(timezone.utc)
tomorrow_this_time = today + timedelta(days=1)

"""
Including `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours`, and `weeks`.

You can also format times to show them to users:
"""

from datetime import datetime, timezone

today = datetime.now(timezone.utc)
print(today.strftime('%Y-%m-%d %H:%M'))  # string format time

"""
You can also take a string and turn it into a `datetime` object:
"""

from datetime import datetime

user_date = input('Enter the date in YYYY-mm-dd format: ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')  # string parse time

print(user_date)

"""
For a cheatsheet on date parsing and formatting, check the resources section of this lecture! I’ll be attached there as a PDF.
"""