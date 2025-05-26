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