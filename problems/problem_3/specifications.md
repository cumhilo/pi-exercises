# Especificaciones: Conversión a Números Romanos

**Descripción:**

Convierte un entero en el rango 1...3999 a su representación en números romanos.

**Parámetros:**

* `number`: entero a convertir. Debe cumplir $1 \leq \text{number} \leq 3999$.

**Retorna:**

* Cadena con la representación en números romanos según las siguientes correspondencias:
    * M = 1000
    * CM = 900
    * D = 500
    * CD = 400
    * C = 100
    * XC = 90
    * L = 50
    * XL = 40
    * X = 10
    * IX = 9
    * V = 5
    * IV = 4
    * I = 1

**Lanza:**

* `ValueError`: si number está fuera del rango [1, 3999].