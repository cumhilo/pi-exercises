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