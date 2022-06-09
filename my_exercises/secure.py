import re
"""
Our definition of a secure filename is:
- The filename must start with an English letters or a number (a-zA-Z0-9).
- The filename can **only** contain English letters, numbers and symbols among these four: `-_()`.
- The filename must end with a proper file extension among `.jpg`, `.jpeg`, `.png` and `.gif`
"""


def is_filename_safe(filename):
    # you only need to change the regular expression (regex) below
    regex = '^[A-Za-z0-9]+[A-Za-z0-9-_()]*\.(jpg|jpeg|png|gif)$'
    return re.match(regex, filename) is not None

