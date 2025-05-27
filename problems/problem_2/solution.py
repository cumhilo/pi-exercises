import re

compiled_patterns = [re.compile(p) for p in [
    r"[A-Z]",
    r"[a-z]",
    r"\d",
    r"[^\w\s]"
]]
space_pattern = re.compile(r"\s")


def check_password(password: str) -> bool:
    if len(password) < 8:
        return False

    passed = 0
    required = 3
    for pattern in compiled_patterns:
        if passed == required:
            break

        if re.search(pattern, password):
            passed += 1

    has_spaces = re.search(space_pattern, password)
    is_secure = passed >= required

    if is_secure and not has_spaces:
        return True

    return False