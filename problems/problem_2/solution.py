import re

def check_password(password: str) -> bool:
    if len(password) < 8:
        return False

    # truly this isn't necessary; looks good to me, making it easier to modify and add patterns, but
    # in some way it's abuse of recursion more than expected
    tests = sum(bool(re.search(i, password)) for i in [
        r"[A-Z]",
        r"[a-z]",
        r"\d",
        r"[^\w\s]"
    ])

    has_spaces = re.search(r"\s", password)

    is_secure = tests >= 3

    if is_secure and not has_spaces:
        return True

    return False
