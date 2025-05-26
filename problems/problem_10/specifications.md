# Especificaciones: Suma de Enteros como Listas de Dígitos

**Descripción:**

Suma dos números enteros representados como listas de dígitos y devuelve el resultado también como lista de dígitos.

**Parámetros:**

* `a`: lista de dígitos (0–9) que representa un entero no negativo. El dígito más significativo está en `a[0]`.
* `b`: lista de dígitos (0–9) que representa otro entero no negativo. El dígito más significativo está en `b[0]`.

**Retorna:**

* Lista de dígitos que representa la suma de los dos enteros (sin ceros iniciales, salvo que el resultado sea 0).

**Precondición:**

* Cada elemento de `a` y de `b` es un entero entre 0 y 9.
* `a` y `b` no están vacías.

**Poscondición:**

* El resultado es la representación en base 10 de $(\text{valor}(a) + \text{valor}(b))$, donde
    $$\text{valor}([d_0, d_1, ..., d_k]) = d_0 \cdot 10^k + d_1 \cdot 10^{k-1} + ... + d_k \cdot 10^0$$
* No hay ceros a la izquierda en la lista resultante, salvo que el número sea 0 (entonces se retorna `[0]`).