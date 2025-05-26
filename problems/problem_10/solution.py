def add_digit_arrays(a: list[int], b: list[int]) -> list[int]:
    p = lambda y: 10 ** y
    rev = lambda lst: enumerate(reversed(lst))
    digits = lambda lst: [int(i) for i in lst]

    return digits(str(sum(a * p(i) for i, a in rev(a)) + sum(b * p(i) for i, b in rev(b))))

# More inaccuracies in large quantities
# def add_digit_arrays(a: list[int], b: list[int]) -> list[int]:
#     return [int(c) for c in str(int("".join([str(_) for _ in a])) + int("".join([str(_) for _ in b])))]

# def add_digit_arrays(a: list[int], b: list[int]) -> list[int]:
#     x = 0
#     for i, a in enumerate(reversed(a)):
#         x += a * (10 ** i)
#
#     for i, a in enumerate(reversed(b)):
#         x += a * (10 ** i)
#
#     result = []
#     for c in str(x):
#         result.append(int(c))
#
#     return result