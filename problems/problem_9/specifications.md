# Especificaciones: Decodificación de Mensaje con Índices

**Descripción:**

Decodifica un mensaje usando un arreglo de índices.

**Precondición:**

* `len(a) == len(b) == n`
* `a` contiene una permutación de los enteros $0...n-1$.
* Si no se cumple la precondición, se lanza `ValueError`.

**Parámetros:**

* `a`: lista de enteros de longitud $n$.
* `b`: lista de caracteres de longitud $n$.
* `n`: tamaño de los arreglos.

**Retorna:**

* Cadena de longitud $n$ formada por los caracteres de `b` reordenados según los números de `a`.

**Excepciones:**

* `ValueError("Longitudes inválidas")`: si `len(a) != n` o `len(b) != n`.
* `ValueError("a no es permutación de 0...n-1")`: si `a` no contiene exactamente los números $0, 1, ..., n-1$.