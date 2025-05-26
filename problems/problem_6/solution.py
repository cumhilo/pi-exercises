def saddle_points(matrix: list[list[int]]) -> list[tuple[int, int]]:
    if not matrix:
        raise ValueError("Matrix is empty")

    result = []
    cache = {}
    # transposed = [*zip(*matrix)]

    k_length = len(matrix[0])

    for i, row in enumerate(matrix):

        mn = min(row)
        if len(row) != k_length:
            raise ValueError("Matrix isn't length consistent")

        for r, c in zip(enumerate(row), zip(*matrix)):
            cache.setdefault(c, max(c))

            x = r[1]
            # cache[0] = max element in column
            # mn = min element in row
            if x == cache[c] and x == mn:
                # result.append((r[0], i)) # column | row
                result.append((i, r[0]))  # row | column

    return result
