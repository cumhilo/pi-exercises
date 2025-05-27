import re

in_between = lambda number, x, y: x <= number <= y

username_pattern = re.compile(r"^([a-z]|[A-Z])\w{5,11}$")  # compile it once

"""
░░░██╗░██╗░░░███╗░░
██████████╗░████║░░
╚═██╔═██╔═╝██╔██║░░
██████████╗╚═╝██║░░
╚██╔═██╔══╝███████╗
░╚═╝░╚═╝░░░╚══════╝
"""


def is_valid_username_regex(username: str) -> bool:  # with regex
    return re.fullmatch(username_pattern, username) is not None


"""
░░░██╗░██╗░██████╗░
██████████╗╚════██╗
╚═██╔═██╔═╝░░███╔═╝
██████████╗██╔══╝░░
╚██╔═██╔══╝███████╗
░╚═╝░╚═╝░░░╚══════╝
"""

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


"""
░░░██╗░██╗░██████╗░
██████████╗╚════██╗
╚═██╔═██╔═╝░█████╔╝
██████████╗░╚═══██╗
╚██╔═██╔══╝██████╔╝
░╚═╝░╚═╝░░░╚═════╝░
"""


def to_roman_numeral(number: int) -> str:
    if not in_between(number, 1, 3999):
        raise ValueError("out of range")

    conversor = {
        1000: "M",
        900: "CM", 500: "D", 400: "CD", 100: "C",
        90: "XC", 50: "L", 40: "XL", 10: "X",
        9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    roman = ""

    for k, v in conversor.items():
        appearances = number // k
        if appearances == 0: continue

        roman += v * appearances
        number -= (k * appearances)

    return roman


"""
░░░██╗░██╗░░░██╗██╗
██████████╗░██╔╝██║
╚═██╔═██╔═╝██╔╝░██║
██████████╗███████║
╚██╔═██╔══╝╚════██║
░╚═╝░╚═╝░░░░░░░░╚═╝
"""


def is_perfect(n: int) -> bool:
    if n < 1:
        raise ValueError("n must be greater than 1")

    if n == 1:
        return False

    return sum(i for i in range(1, n) if n % i == 0) == n


def list_perfect_numbers(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be greater than 1")

    return [i for i in range(1, n + 1) if is_perfect(i)]


from datetime import datetime as dt

"""
░░░██╗░██╗░███████╗
██████████╗██╔════╝
╚═██╔═██╔═╝██████╗░
██████████╗╚════██╗
╚██╔═██╔══╝██████╔╝
░╚═╝░╚═╝░░░╚═════╝░
"""

date_pattern = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def read_valid_dates(file_path: str) -> list[str]:
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        raise FileNotFoundError(f"Specified path: '{file_path}' doesn't exists")

    dates = []
    for i, line in enumerate(f):
        line = line.strip()

        if date_pattern.fullmatch(line) is None:
            print(error_date(i, line, "it doesn't match de pattern dd/mm/yyyy"))
            continue

        try:
            date = dt.strptime(line, "%d/%m/%Y")
            dates.append(date)
        except ValueError as e:
            print(error_date(i, line, e))

    dates.sort()
    return [d.date().isoformat() for d in dates]


def error_date(index, line, reason) -> str:
    return f"WARNING | Malformed line #{index} @ ({line}) due {reason}"


"""
░░░██╗░██╗░░█████╗░
██████████╗██╔═══╝░
╚═██╔═██╔═╝██████╗░
██████████╗██╔══██╗
╚██╔═██╔══╝╚█████╔╝
░╚═╝░╚═╝░░░░╚════╝░
"""


def saddle_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    if not matrix:
        raise ValueError("Matrix is empty")

    result = []
    cache = {}

    k_length = len(matrix[0])

    for i, row in enumerate(matrix):

        mn = min(row)
        if len(row) != k_length:
            raise ValueError("Matrix isn't length consistent")

        for r, c in zip(enumerate(row), zip(*matrix)):
            cache.setdefault(c, max(c))

            x = r[1]
            # cache[c] = max element in column
            # mn = min element in row
            if x == cache[c] and x == mn:
                # result.append((r[0], i)) # column | row
                result.append((i, r[0]))  # row | column

    return result


"""
░░░██╗░██╗░███████╗
██████████╗╚════██║
╚═██╔═██╔═╝░░░░██╔╝
██████████╗░░░██╔╝░
╚██╔═██╔══╝░░██╔╝░░
░╚═╝░╚═╝░░░░░╚═╝░░░
"""


def is_magic_square(matrix: list[list[int]]) -> bool:
    if not matrix:
        raise ValueError("Matrix is empty")

    length = len(matrix)

    # if not all(len(lst) == length for lst in matrix):
    #     return False

    matrix_0 = matrix[0]

    if len(matrix_0) != length:
        raise error()

    magic_k = sum(matrix_0)
    left_diagonal = []
    right_diagonal = []

    for lst, i in zip(matrix, range(0, length)):
        # checking shape
        if len(lst) != length:
            raise error()

        if sum(lst) != magic_k:
            return False

        left_diagonal.append(lst[i])
        right_diagonal.append(lst[(length - 1) - i])

    if not sum(left_diagonal) == magic_k or not sum(right_diagonal) == magic_k:
        return False

    return True


def error() -> ValueError:
    return ValueError("Matrix must be square")


"""
░░░██╗░██╗░░█████╗░
██████████╗██╔══██╗
╚═██╔═██╔═╝╚█████╔╝
██████████╗██╔══██╗
╚██╔═██╔══╝╚█████╔╝
░╚═╝░╚═╝░░░░╚════╝░
"""


# Due to the fact python make things so easy, doing this (not using libraries, only python native) should be
# the most efficient algorithm

def merge_sorted_arrays(a: list[int], b: list[int]) -> list[int]:
    merged = a + b
    merged.sort()

    return merged


# Here's other implementation
# if we consider that they are already ordered, we can put them together little by little.
# which may be the one they were looking for.

def merge_sorted_arrays_1(a: list[int], b: list[int]) -> list[int]:
    l_a = len(a)
    l_b = len(b)

    size = l_a + l_b
    result = [0] * size

    a_i, b_i = 0, 0
    for i in range(size):

        if not a_i >= l_a and not b_i >= l_b:
            if a[a_i] < b[b_i]:
                result[i] = a[a_i]
                a_i += 1
            else:
                result[i] = b[b_i]
                b_i += 1
        else:
            if b_i >= l_b:
                result[i] = a[a_i]
                a_i += 1
            else:
                result[i] = b[b_i]
                b_i += 1

    return result


# Here's other implementation if we don't consider arrays are sorted
# I'll use a kind of bubble sorting 'cause it's easier, not the most efficient

def merge_sorted_arrays_2(a: list[int], b: list[int]) -> list[int]:
    # Merging arrays # 1
    # merged = []
    # for i in a:
    #     merged.append(i)
    #
    # for i in b:
    #     merged.append(i)

    # Merging arrays # 2
    merged = a + b

    # Sorting it
    while True:
        x = is_sorted(merged)

        if x[0]:
            break

        merged = sort(merged, x[1])

    return merged


def sort(lst: list[int], start: int) -> list[int]:
    length = len(lst)
    if length < 2:
        return lst

    fixed_size = length - 1
    if start == fixed_size:
        return lst

    if not (0 <= start < length):
        raise ValueError("Not a valid start index")

    r = range(start, length)
    for k in r:
        v = lst[k]
        nxt = k + 1

        if nxt in r:
            cache = lst[nxt]
            if cache < v:
                lst[nxt] = v
                lst[k] = cache

    return lst


def is_sorted(lst: list[int]) -> (bool, int):
    length = len(lst)
    if length < 2:
        return True

    x = lst[0]
    for i, e in enumerate(lst):
        if e < x:
            return False, i - 1

        x = e

    return True, length


"""
░░░██╗░██╗░░█████╗░
██████████╗██╔══██╗
╚═██╔═██╔═╝╚██████║
██████████╗░╚═══██║
╚██╔═██╔══╝░█████╔╝
░╚═╝░╚═╝░░░░╚════╝░
"""

def decode(a: list[int], b: list[str], n: int) -> str:
    if len(a) != len(b) or len(a) != n:
        raise ValueError("Longitudes inválidas")  # ValueError("length must be equal")

    r = range(n)

    if len(set(a)) != len(a):
        raise ValueError("a no es permutación de 0...n-1")  # ValueError("there's an element which isn't a permutation")

    return "".join(b[a[i]] if (a[i] in r) else fail(i) for i in r)


# More readable if you're not accustomed to python (but using join is most efficient)
def decode_1(a: list[int], b: list[str], n: int) -> str:
    if len(a) != len(b) or len(a) != n:
        raise ValueError("length must be equal")

    if len(set(a)) != len(a):
        raise ValueError("there's an element which isn't a permutation")

    r = range(n)
    s = ""

    for i in r:
        x = a[i]
        if not x in r:
            fail()

        l = b[x]
        s += l

    return s


def fail():
    raise ValueError(
        "a no es permutación de 0...n-1")  # ValueError(f"'A' has a permutation ({index}) which is not valid")


"""
░░░██╗░██╗░░░███╗░░░█████╗░
██████████╗░████║░░██╔══██╗
╚═██╔═██╔═╝██╔██║░░██║░░██║
██████████╗╚═╝██║░░██║░░██║
╚██╔═██╔══╝███████╗╚█████╔╝
░╚═╝░╚═╝░░░╚══════╝░╚════╝░
"""


def add_digit_arrays(a: list[int], b: list[int]) -> list[int]:
    p = lambda y: 10 ** y
    rev = lambda lst: enumerate(reversed(lst))
    digits = lambda lst: [int(i) for i in lst]

    return digits(str(sum(a * p(i) for i, a in rev(a)) + sum(b * p(i) for i, b in rev(b))))
