def add_digit_arrays(a: list[int], b: list[int]) -> list[int]:
    return [int(r) for r in str(sum(a * (10 ** i) for i, a in enumerate(reversed(a))) + sum(b * (10 ** i) for i, b in enumerate(reversed(b))))]

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