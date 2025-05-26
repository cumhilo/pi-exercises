# Especificaciones: Validación de Contraseña

**Descripción:**

Comprueba si ‘password’ cumple las reglas de validez.

**Reglas de Validación:**

1.  Longitud mínima de 8 caracteres.
2.  No contiene espacios en blanco.
3.  Incluye al menos tres de los siguientes tipos de caracteres:
    * Letras mayúsculas (A–Z)
    * Letras minúsculas (a–z)
    * Dígitos (0–9)
    * Símbolos (por ejemplo: #, @, ?, $, %, &, –, +, etc.)

**Parámetros:**

* `password`: cadena que representa la contraseña a validar.

**Retorna:**

* `True`: si la contraseña cumple los tres requisitos.
* `False`: en caso contrario.