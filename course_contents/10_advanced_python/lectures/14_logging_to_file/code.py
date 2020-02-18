"""
In its simplest term, the `logging` module is used to print things out (to the console or to a file).

The `logging` module should be used to communicate with the developer (e.g. information about what’s happening; when an error happens; a critical problem; etc…).

To communicate with the user, continue using `print()` and `input()`.

To use logging, we just have to import the `logging` module and get a new logger:
"""

import logging

logger = logging.getLogger('test_logger')

logger.info("This won't show up.")
logger.warning('This will.')

"""
There are various logging levels (below in ascending order of criticality), for you to use depending on the circumstance:

DEBUG
INFO
WARNING
ERROR
CRITICAL

So if you’re logging for help while developing or debugging, use the `DEBUG` level (`logger.debug('message')`).

If your program’s about to crash because a critical exception happened; use `logger.critical()`.

You can configure the output so all messages are shown, not just warning and above:
"""

logging.basicConfig(level=logging.DEBUG)

"""
You can configure the output to include more than just the level and the logger used. You can add for example the time:
"""

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)

"""
Or below, an example of a great way to configure your logger for maximum readability and usefulness.

Of course, as you go through your Python journey you may encounter situations where using a differently-configured logger would be better. Or when you’ll work with people who want logging in a particular way.

You’ll then have to decide how you want to log things, and as most things in software that should be a team decision.
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG)

logger = logging.getLogger('my_app')
logger.debug("This is a debug log")
logger.info("This is an info log")
logger.critical("This is critical")
logger.error("An error occurred")

"""
And if you wanted your applications logs to go to a file instead of the console, do something like this:
"""

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

"""
If you call `logging.getLogger('my_app')` from many different files, you’ll always get the same `Logger` object—so any configuration changes and the handler added will be reflected throughout all the app.

If you want to use a different name but want the configuration to be kept between handlers, the best way is to create child handlers:
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt')

logger = logging.getLogger('my_app')

another_logger = logging.getLogger('my_app.database')  # gets a child logger called 'database' of 'my_app'

"""
Add logging to your projects moving forward! It’s great when you can trace what was happening in your system as it happened with extensive logs (although, it does mean the code will be longer since you need to include logging statements everywhere).
"""