# Especificaciones: Encontrar Puntos Silla en una Matriz

**Descripción:**

Encuentra todos los puntos silla de una matriz de enteros. Un punto silla es un elemento que es el máximo en su fila y el mínimo en su columna (o viceversa: mínimo en su fila y máximo en su columna).

**Parámetros:**

* `matrix`: lista de listas de enteros, de tamaño $m \times n$ ($m \geq 1$, $n \geq 1$). Se asume que cada fila tiene la misma longitud.

**Retorna:**

* Lista de tuplas $(i, j)$ con las coordenadas de cada punto silla:
    * $i$: índice de fila ($0 \leq i < m$)
    * $j$: índice de columna ($0 \leq j < n$)
    El orden de las tuplas no importa. Si no hay puntos silla, retorna lista vacía.

**Lanza:**

* `ValueError`: si `matrix` está vacía o no es “rectangular” (filas de diferente longitud).