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