import re

from problems.utils import in_between


def is_valid_username(username: str) -> bool:  # without regex
    if not in_between(len(username), 6, 12):
        return False

    # String#isalpha() might cause problems due external alphabets, instead we can create a "ABCDE...Z" str and check if c is in the str,
    # but it's more inefficient
    if not (username[0].isalpha()):
        return False

    for c in username:
        if not (c.isalpha() or c.isdigit() or c == '_'):
            return False

    return True


# REGEX ALGORITHM
pattern = re.compile(r"^([a-z]|[A-Z])\w{5,11}$")  # compile it once


def is_valid_username_regex(username: str) -> bool:  # with regex
    # we can improve the performance by adding the checks before the for in the is_valid_username()
    return re.fullmatch(pattern, username) is not None
