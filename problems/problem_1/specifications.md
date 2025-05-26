# Especificaciones: Validación de Nombre de Usuario

**Descripción:**

Comprueba si ‘username’ cumple las reglas de validez.

**Reglas de Validación:**

1.  Longitud entre 6 y 12 caracteres (ambos inclusive).
2.  Sólo letras (a–z, A–Z), dígitos (0–9) o guión bajo (_).
3.  Debe comenzar con una letra (a–z, A–Z).

**Parámetros:**

* `username`: cadena a validar.

**Retorna:**

* `True`: si username es válido según las reglas.
* `False`: en caso contrario.