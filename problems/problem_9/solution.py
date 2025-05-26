# if sum(a) != sum(r):
# Esto es una genialidad jajaja

# Para test como:
# try:
#     decode([0, 0, 2], ['a','b','c'], 3)
#     assert False, "Expected ValueError for invalid permutation"
# except ValueError:
#     pass

# Esto sucede porque por ejemplo si 0, 0, 2 entonces sum(a) != sum(r), puesto que (2 != 3) == True,
# si intentamos suplir la suma en el rango algo como 0, 0, 3 para que sum(a) != sum(r) (3 != 3) == False
# luego en el bucle for i in r, como a[i] (en este caso 3) no forma parte del rango, entonces dará un error.

# Sin embargo; para casos como print(decode([0, 2, 0, 2], ["A", "B", "C", "D"], 4)) no funciona.
# NOTA: Escribí este comentario en español debido a lo extenso que es, no es una inconsistencia.

def decode(a: list[int], b: list[str], n: int) -> str:
    if len(a) != len(b) or len(a) != n:
        raise ValueError("Longitudes inválidas") # ValueError("length must be equal")

    r = range(n)

    # As sum(r) is equal to (n - 1) * n / 2 (but most inefficient)
    # I've changed it from: "sum(a) != sum(r):" to "sum(a) != ((n - 1) * n / 2)"
    # slightly less readable but more efficient

    if len(set(a)) != len(a):  # (sum(a) != ((n - 1) * n // 2))
        raise ValueError("a no es permutación de 0...n-1") # ValueError("there's an element which isn't a permutation")

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
            fail(i)

        l = b[x]
        s += l

    return s


def fail(index: int):
    raise ValueError("a no es permutación de 0...n-1") # ValueError(f"'A' has a permutation ({index}) which is not valid")
