# Especificaciones: Números Perfectos en un Intervalo

**Descripción:**

Devuelve todos los números perfectos en el intervalo $[1, n]$, ordenados de menor a mayor. Un número perfecto es aquel que es igual a la suma de sus divisores propios (todos los divisores positivos excepto él mismo).

**Parámetros:**

* `n`: límite superior del intervalo (entero positivo).

**Retorna:**

* Lista de enteros que son números perfectos entre 1 y $n$ inclusive, en orden ascendente.

**Lanza:**

* `ValueError`: si $n < 1$.