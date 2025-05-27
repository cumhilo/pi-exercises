# [🚧] Errores

> [!WARNING]
> Problema #5 (Read valid dates)

* Se menciona en la descripción del problema el siguiente enunciado

> ValueError si alguna línea no puede ser interpretada como fecha (por ejemplo, formato mal formado).

No obstante, esto carece de sentido. Si seguimos estrictamente las normas con
las [fechas dadas](./problems/tests/fechas.txt), se producirían multiples errores que impedirian el flujo normal del
programa.
En su defecto si esa era la intención debería lanzarse un **RuntimeError** que no impidiera el flujo normal del programa

Sin irnos muy lejos, la fecha `15/13/2021` debería lanzar una excepción puesto que su mes no está dentro de los
límites.  
Al igual que la fecha `"5/5/2020"` puesto que carece del formato `dd/mm/yyyy`

Por lo tanto no es realmente válido lanzar un **ValueError** en dichas circustancias!


> [!WARNING]
> Problema #6 (Saddle points)

* En el inciso N.º 1, del problema de los puntos sillas de una matriz se da el siguiente input:

```python
matrix = [
    [3, 1, 3],
    [3, 2, 4],
    [2, 5, 4]
]

print(saddle_points(matrix))
```

se espera que el output sea

```python
[(0, 2)]
```

Sin embargo esto se da por tomar una definición erronea del punto silla.

Notemos que https://en.m.wikipedia.org/wiki/Saddle_point en la sección #other-uses
> A saddle point of a matrix is an element which is both the largest element in its column and the smallest element in
> its row.

Si miramos detalladamente la matriz notaremos que el punto (0, 2) es el mayor elemento en su fila y el menor en su fila
lo cual **es contrario a la definición mencionada**



> [!WARNING]
> Problema #9 (Decode)

* La llamada a la función decode:

```python
decode([1, 2, 0, 5, 3, 4, 6], ['c', 's', 'e', 'o', 'e', 'r', 't'], 7)
```

En teoría debe retornar la palabra `secreto`; sin embargo, esto no es cierto.
Siguiendo estrictamente la lógica mencionada en la descripción del problema este debería retornar`secroet`.

Podemos notarlo rápidamente ya que en `a = [1,2,0,5,3,4,6]`, el último index, `a[-1]` = 6 y
`b = ['c','s','e','o','e','r','t']`, donde `b[-1] = t` por lo tanto en nuestro resultado final debería aparecer,
`??????t`   como último elemento de la cadena. Lo cual es carente de sentido!