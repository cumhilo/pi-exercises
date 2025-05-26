# Especificaciones: Filtrado y Formateo de Fechas

**Descripción:**

Lee un archivo de texto con una fecha por línea en formato "dd/mm/yyyy", filtra las fechas válidas según las reglas, y devuelve la lista de fechas válidas ordenadas de forma ascendente, en formato "yyyy-mm-dd".

**Parámetros:**

* `file_path`: ruta al archivo de texto que contiene fechas, una por línea, en el formato "dd/mm/yyyy".

**Retorna:**

* Lista de cadenas con las fechas válidas, convertidas al formato ISO “yyyy-mm-dd” y ordenadas cronológicamente.

**Lanza:**

* `FileNotFoundError`: si no existe `file_path`.
* `ValueError`: si alguna línea no puede ser interpretada como fecha (por ejemplo, formato mal formado).