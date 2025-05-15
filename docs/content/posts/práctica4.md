+++
date = '2025-05-10T22:27:51-07:00'
draft = false
title = 'Práctica 4'
+++

## Tabla de contenido

- [Prolog y el paradigma lógico](#prolog-y-el-paradigma-lógico)
- [Paradigma lógico](#paradigma-lógico)
- [Prolog](#prolog)
- [Tutorial de Prolog](#tutorial-de-prolog)
  - [1. Introducción a Prolog](#1-introducci%C3%B3n-a-prolog)
  - [2. Instalación de Prolog](#2-instalaci%C3%B3n-de-prolog)
  - [3. "¡Hola, mundo!" en Prolog](#3-hola-mundo-en-prolog)
  - [4. Las bases de Prolog](#4-las-bases-de-prolog)
  - [5. Relaciones](#5-relaciones)
    - [5.1. Ejemplo práctico (Familia)](#51-ejemplo-pr%C3%A1ctico-familia)
  - [6. Objetos de datos](#6-objetos-de-datos)
    - [6.1. Átomos](#61-%C3%A1tomos)
    - [6.2. Números](#62-n%C3%BAmeros)
    - [6.3. Variables](#63-variables)
    - [6.4. Variables anónimas](#64-variables-an%C3%B3nimas)
  - [7. Operadores](#7-operadores)
    - [7.1. Operadores comparativos](#71-operadores-comparativos)
    - [7.2. Operadores aritméticos](#72-operadores-aritm%C3%A9ticos)
  - [8. Ciclos y decisiones](#8-ciclos-y-decisiones)
    - [8.1. Ciclos](#81-ciclos)
    - [8.2. Decisiones](#82-decisiones)
  - [9. Conjunciones y disyunciones](#9-conjunciones-y-disyunciones)
  - [10. Listas](#10-listas)
    - [10.1. Operaciones básicas con listas](#101-operaciones-b%C3%A1sicas-con-listas)
    - [10.1.1. Comprobación de miembro](#1011-comprobaci%C3%B3n-de-miembro)
    - [10.1.2. Cálculo de longitud](#1012-c%C3%A1lculo-de-longitud)
    - [10.1.3. Concatenación](#1013-concatenaci%C3%B3n)
    - [10.1.4. Borrar elemento de una lista](#1014-borrar-elemento-de-una-lista)
    - [10.1.5. Agregar elemento a una lista](#1015-agregar-elemento-a-una-lista)
    - [10.1.6. Insertar elemento en una lista](#1016-insertar-elemento-en-una-lista)
    - [10.1.7 Muchas otras operaciones](#1017-muchas-otras-operaciones)
  - [11. Recursión y estructuras](#11-recursi%C3%B3n-y-estructuras)
    - [11.1. Recursión](#111-recursi%C3%B3n)
    - [11.2. Estructuras](#112-estructuras)
  - [12. Retroceso](#12-retroceso)
  - [13. Diferente y negación](#13-diferente-y-negaci%C3%B3n)
  - [14. Entradas y salidas](#14-entradas-y-salidas)
  - [15. Predicados predefinidos](#15-predicados-predefinidos)
  - [16. Estructura de árbol (caso de estudio)](#16-estructura-de-%C3%A1rbol-caso-de-estudio)

## Prolog y el paradigma lógico

En este artículo y práctica se explorará el lenguaje de programación Prolog, que se basa en el paradigma lógico.

## Paradigma lógico

El paradigma lógico se basa en la idea de que los programas son conjuntos de declaraciones lógicas. En lugar de describir cómo realizar una tarea, como en los lenguajes imperativos, se describe qué es cierto y se deja que el sistema deduzca cómo llegar a esas conclusiones.

## Prolog

Prolog es un lenguaje de programación que se basa en el cálculo de predicados y la lógica de primer orden. Se utiliza ampliamente en inteligencia artificial, procesamiento de lenguaje natural y sistemas expertos.

## Tutorial de Prolog

A continuación se presenta un tutorial básico de Prolog.

### 1. Introducción a Prolog

El nombre Prolog proviene de "LOGical PROgramming", o programación lógica. A diferencia de otros lenguajes de programación como C, Java, Python, Haskell, etc., Prolog no se basa en la ejecución de instrucciones secuenciales o en recursión y funciones. En su lugar, Prolog se basa en la lógica de primer orden y en la resolución de problemas a través de la deducción lógica.

El núcleo de Prolog es un motor de inferencia que utiliza un algoritmo de resolución para deducir nuevos hechos a partir de los hechos y reglas existentes. Prolog permite expresar relaciones entre objetos y realizar consultas sobre esas relaciones.

Los hechos en Prolog se representan como predicados, que son declaraciones que describen una relación entre uno o más objetos. Por ejemplo, el hecho "Juan es un hombre" se puede representar como:

```prolog
hombre(juan).
```

Las reglas se utilizan para definir relaciones más complejas y se expresan en forma de implicaciones. Por ejemplo, la regla "Si X es un hombre, entonces X es mortal" se puede representar como:

```prolog
mortal(X) :- hombre(X).
```

### 2. Instalación de Prolog

Para instalar Prolog, puedes seguir estos pasos:

1. **Descargar SWI-Prolog**: Ve al sitio web oficial de [SWI-Prolog](https://www.swi-prolog.org/) y descarga la versión adecuada para tu sistema operativo.
2. **Instalar SWI-Prolog**: Sigue las instrucciones de instalación para tu sistema operativo.
3. **Verificar la instalación**: Abre una terminal o símbolo del sistema y escribe `swipl`. Si ves el prompt de Prolog, la instalación fue exitosa.

Alternativamente, puedes usar el entorno en línea de [SWI-Prolog](https://swish.swi-prolog.org/) para practicar sin necesidad de instalar nada.

### 3. "¡Hola, mundo!" en Prolog

Escribe el siguiente comando para entrar al intérprete de Prolog:

```bash
swipl
```

Luego, puedes escribir el siguiente código para imprimir "¡Hola, mundo!" en la consola:

```prolog
write('¡Hola, mundo!').
```

Esto mostrará el mensaje en la consola. Todas las oraciones en Prolog deben terminar con un punto. Nota como se despliega el mensaje `¡Hola, mundo!` en la consola, seguido de un `true.`.

Para salir del intérprete de Prolog, puedes usar el comando `halt.`, o presionar `Ctrl+C`.

Alternativamente, es más recomendable escribir el código en un archivo de texto con extensión `.pl`, por ejemplo `holamundo.pl`. Intenta crear un archivo con el siguiente contenido:

```prolog
main :- write('¡Hola, mundo!').
```

Guarda el archivo, abre `swipl` y carga el archivo con el siguiente comando:

```prolog
[holamundo].
```

Esto cargará el archivo y podrás ejecutar el predicado `main` escribiendo:

```prolog
?- main.
```

Esto ejecutará el predicado `main`, que a su vez ejecutará el comando `write('¡Hola, mundo!')`. Si todo está correcto, deberías ver "¡Hola, mundo!" en la consola.

Se puede usar `%` para comentar líneas en Prolog. Por ejemplo:

```prolog
% Este es un comentario
write('¡Hola, mundo!'). % Este es otro comentario
```

También puedes usar `/* ... */` para comentarios de varias líneas:

```prolog
/* Este es un comentario
   de varias líneas */
```

Adicionalmente, dentro de un archivo, puedes usar `,` para separar múltiples predicados en una sola línea:

```prolog
write('¡Hola, mundo!'), write('¡Hola, Prolog!').
```

Esto ejecutará ambos predicados en una sola línea.

Por último, puedes usar `nl` para imprimir una nueva línea:

```prolog
write('¡Hola, mundo!'), nl, write('¡Hola, Prolog!').
```

### 4. Las bases de Prolog

La base de conocimiento de Prolog se compone de hechos y reglas. Los hechos son afirmaciones sobre el mundo, mientras que las reglas son inferencias que se pueden hacer a partir de los hechos.

Los hechos se representan como predicados, que son declaraciones que describen una relación entre uno o más objetos. Por ejemplo, el hecho "Juan es un hombre" se puede representar como:

```prolog
hombre(juan).
```

Las reglas se utilizan para definir relaciones más complejas y se expresan en forma de implicaciones. Por ejemplo, la regla "Si X es un hombre, entonces X es mortal" se puede representar como:

```prolog
mortal(X) :- hombre(X).
```

Los predicados pueden tener uno o más argumentos, que son los objetos sobre los que se aplica la relación. Por ejemplo, el predicado `padre` puede tener dos argumentos: el padre y el hijo.

```prolog
padre(juan, maria).
padre(juan, pedro).
```

Esto significa que Juan es el padre de María y Pedro.

Los predicados también pueden ser recursivos, lo que significa que pueden definirse en términos de sí mismos. Por ejemplo, el predicado `abuelo` se puede definir como:

```prolog
abuelo(X, Y) :- padre(X, Z), padre(Z, Y).
```

Esto significa que X es el abuelo de Y si X es el padre de Z y Z es el padre de Y.

Podemos utilizar consultas para preguntar a Prolog sobre los hechos y reglas en la base de conocimiento. Por ejemplo, podemos preguntar si Juan es un hombre:

```prolog
?- hombre(juan).
```

Esto devolverá `true` si Juan es un hombre, o `false` si no lo es.

También podemos preguntar si Juan es el padre de María:

```prolog
?- padre(juan, maria).
```

Esto devolverá `true` si Juan es el padre de María, o `false` si no lo es.
Podemos hacer consultas más complejas utilizando variables. Por ejemplo, podemos preguntar quiénes son los hijos de Juan:

```prolog
?- padre(juan, X).
```

Esto devolverá todos los valores de X que satisfacen la relación `padre(juan, X)`, es decir, todos los hijos de Juan.

Es recomendable guardar una base de conocimiento en un archivo `.pl` y cargarlo en Prolog para trabajar con él.

### 5. Relaciones

El verdadero poder de Prolog radica en su capacidad para trabajar con relaciones. Podemos definir una cantidad considerable de predicados y reglas para representar relaciones complejas entre objetos.

Por ejemplo, podemos definir una relación entre dos hermanos:

```prolog
hermano(X, Y) :- padre(Z, X), padre(Z, Y), X \= Y.
padre(juan, maria).
padre(juan, pedro).
```

Como resultado, podemos preguntar si María y Pedro son hermanos:

```prolog
?- hermano(maria, pedro).
```

Esto devolverá `true` porque María y Pedro tienen el mismo padre, Juan, por lo tanto, cumplen con la primera regla, incluso si no se especifica explícitamente que son hermanos, Prolog deduce que lo son.

#### 5.1. Ejemplo práctico (Familia)

```prolog
% familia.pl
female(pam).
female(liz).
female(pat).
female(ann).

male(jim).
male(bob).
male(tom).
male(peter).

parent(pam, bob).
parent(tom, bob).
parent(tom, liz).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).
parent(bob, peter).
parent(peter, jim).

mother(X, Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
haschild(X) :- parent(X, _).
sister(X, Y) :- parent(Z, X), parent(Z, Y), female(X), X \= Y.
brother(X, Y) :- parent(Z, X), parent(Z, Y), male(X), X \= Y.
```

Puedes cargar este archivo en Prolog y hacer consultas como:

```prolog
?- parent(X, jim).
X = pat ; % Puedes usar ; para buscar más soluciones
X = peter.
true.
?- mother(X, Y).
X = pam,
Y = bob ;
X = pat,
Y = jim ;
false.
```

### 6. Objetos de datos

Los objetos de datos en Prolog se pueden dividir en varias categorías:

- **Átomos**: `tom`, `pat`, `x100`, `x_45`
- **Números**: `100`, `1235`, `2000.45`
- **Variables**: `X`, `Y`, `Xval`, `_X`
- **Estructuras**: `day(9, jun, 2017)`, `point(10, 25)`

#### 6.1. Átomos

Los átomos son constantes que representan un valor único. Pueden ser palabras, números o símbolos. Los átomos pueden comenzar con una letra minúscula o un símbolo especial, y pueden contener letras, dígitos y guiones bajos. Por ejemplo, `atom`, `atom_1`, `atom-2` son átomos válidos.

#### 6.2. Números

Otra forma de representar constantes son los números. Prolog admite enteros y números de punto flotante. Los números se pueden utilizar en cálculos y comparaciones. El rango normal de los números enteros es de `-16383` a `16383`. También se pueden utilizar números de punto flotante, como `3.14` o `2.71828`.

#### 6.3. Variables

Las variables en Prolog son representadas por letras mayúsculas o por un guion bajo seguido de una letra minúscula. Las variables pueden ser utilizadas para representar cualquier valor y se pueden unificar con otros términos. Por ejemplo, `X`, `Y`, `Z`, `_X`, `_y` son variables válidas.

Las variables pueden ser utilizadas en consultas y reglas para representar valores desconocidos. Por ejemplo, en la consulta `?- padre(X, Y).`, `X` y `Y` son variables que representan el padre y el hijo, respectivamente.

#### 6.4. Variables anónimas

Las variables anónimas se representan con un guion bajo `_`. Estas variables no se pueden unificar con otros términos y se utilizan para representar valores que no son relevantes para la consulta. Por ejemplo, en la consulta `?- padre(_, Y).`, el guion bajo representa un padre desconocido y solo se interesa en el hijo `Y`.

### 7. Operadores

Prolog tiene varios operadores que se pueden utilizar para realizar operaciones lógicas y matemáticas. Algunos son presentes en otros lenguajes de programación, mientras que otros son específicos de Prolog.

#### 7.1. Operadores comparativos

Los operadores comparativos se utilizan para comparar dos valores y devolver un valor booleano (`true` o `false`). Los operadores comparativos en Prolog son:

| Operador  | Descripción              |
|-----------|--------------------------|
| `X > Y`   | X es mayor que Y         |
| `X < Y`   | X es menor que Y         |
| `X >= Y`  | X es mayor o igual que Y |
| `X =< Y`  | X es menor o igual que Y |
| `X =:= Y` | X es igual a Y           |
| `X =\= Y` | X es diferente de Y      |

Algunos ejemplos de uso de operadores comparativos son:

```prolog
?- 5 > 3.
true.
?- 5 < 3.
false.
?- 5 >= 5.
true.
?- 5 =< 3.
false.
?- 5 =:= 5.
true.
?- 5 =\= 3.
true.
```

#### 7.2. Operadores aritméticos

| Operador | Descripción     |
|----------|-----------------|
| `+`      | Suma            |
| `-`      | Resta           |
| `*`      | Multiplicación  |
| `/`      | División        |
| `**`     | Potencia        |
| `//`     | División entera |
| `mod`    | Módulo          |

Se utiliza `is` para evaluar expresiones aritméticas. Por ejemplo, `X is 5 + 3` asigna el valor `8` a `X`. Los operadores aritméticos se utilizan para realizar cálculos matemáticos y se pueden combinar en expresiones más complejas.

Algunos ejemplos de uso de operadores aritméticos son:

```prolog
?- X is 5 + 3.
X = 8.
?- Y is 10 - 2.
Y = 8.
?- Z is 4 * 2.
Z = 8.
?- A is 16 / 2.
A = 8.
?- B is 2 ** 3.
B = 8.
?- C is 10 // 3.
C = 3.
?- D is 10 mod 3.
D = 1.
```

### 8. Ciclos y decisiones

Los ciclos son estructuras de control que permiten repetir un bloque de código varias veces. Las decisiones son estructuras de control que permiten ejecutar un bloque de código solo si se cumple una condición. En Prolog, los ciclos y decisiones se implementan de manera diferente a otros lenguajes de programación.

#### 8.1. Ciclos

No hay estructuras de control de flujo como `for`, `while` o `if` en Prolog. En su lugar, Prolog utiliza recursión para simular ciclos y decisiones. La recursión es una técnica en la que una función se llama a sí misma para resolver un problema.

A continuación se presenta un ejemplo de un ciclo en Prolog:

```prolog
% Ciclo en Prolog
count_to_10(10) :- write(10), nl.
count_to_10(X) :-
    write(X), nl,
    Y is X + 1,
    count_to_10(Y).
```

Este código cuenta del `X` a `10` e imprime cada número en una nueva línea. La función `count_to_10/1` se llama a sí misma con el valor incrementado de `X` hasta que `X` llega a `10`, en dado caso se utiliza la primera regla, que imprime el número `10` y termina la recursión.

Se pueden imprimir los números del `5` al `10` de la siguiente manera:

```prolog
?- count_to_10(5).
5
6
7
8
9
10
true.
```

#### 8.2. Decisiones

Las decisiones en Prolog se implementan utilizando reglas y predicados. Por ejemplo, podemos definir una regla que verifique si un número es par o impar:

```prolog
gt(X, Y) :- X >= Y, write('X is greater than or equal to Y').
gt(X, Y) :- X < Y, write('X is less than Y').
```

Esto define dos reglas: una que se ejecuta si `X` es mayor o igual que `Y`, y otra que se ejecuta si `X` es menor que `Y`. Puedes llamar a esta regla con diferentes valores de `X` y `Y` para ver cómo funciona.

```prolog
?- gt(5, 3).
X is greater than or equal to Y
true.
?- gt(2, 3).
X is less than Y
true.
```

### 9. Conjunciones y disyunciones

En Prolog, las conjunciones y disyunciones se utilizan para combinar múltiples condiciones en una regla o consulta.

La conjunción se representa con la coma `,`, que actúa como un operador lógico "Y". Por ejemplo:

```prolog
sibling(X, Y) :- father(Z, X), mother(Z, Y), X \= Y.
```

Esto significa que `X` es hermano de `Y` si `Z` es padre de ambos y `X` no es igual a `Y`.

La disyunción se representa con el punto y coma `;`, que actúa como un operador lógico "O". Por ejemplo:

```prolog
child_of(X, Y) :- father(Y, X) ; mother(Y, X).
```

Esto significa que `X` es hijo de `Y` si `Y` es padre o madre de `X`.

### 10. Listas

Las listas son una estructura de datos fundamental en Prolog. Se representan con corchetes `[]` y pueden contener cualquier tipo de elemento, incluidos otros términos, números, átomos y variables.

Para representar una lista vacía, se utiliza `[]`. Una lista con uno o más elementos se representa como `[Elemento1, Elemento2, ..., ElementoN]`. Por ejemplo:

```prolog
lista([1, 2, 3, 4]).
lista([a, b, c]).
lista([1, a, 2, b]).
```

Las listas están compuestos de dos partes: la cabeza (el primer elemento) y la cola (el resto de la lista). Se pueden enlazar listas utilizando el operador `|`. Por ejemplo:

```prolog
% lista.pl
lista([Cabeza|Cola]) :- write(Cabeza), write(' '), write(Cola).
```

```prolog
?- lista([1, 2, 3, 4]).
1 [2, 3, 4]
true.
```

Esto imprimirá la cabeza y la cola de la lista.

#### 10.1. Operaciones básicas con listas

Se pueden realizar las siguientes operaciones básicas con listas en Prolog:

| Operación               | Descripción                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| Comprobación de miembro | Durante esta operación, ¿podemos verificar si un elemento pertenece a una lista? |
| Cálculo de longitud     | Con esta operación, podemos encontrar la longitud de una lista.                  |
| Concatenación           | Esta operación nos permite combinar dos listas en una sola.                      |
| Borrar elementos        | Esta operación nos permite eliminar un elemento de una lista.                    |
| Agregar elementos       | Esta operación nos permite agregar un elemento a una lista.                      |
| Insertar elementos      | Esta operación nos permite insertar un elemento en una lista.                    |

##### 10.1.1. Comprobación de miembro

La comprobación de miembro se utiliza para verificar si un elemento pertenece a una lista. Se puede implementar utilizando la siguiente regla:

```prolog
% list_basics.pl
list_member(X, [X|_]). % Con esto verificamos si el elemento es la cabeza de la lista
list_member(X, [_|Tail]) :- list_member(X, Tail). % Con esto verificamos si el elemento es la cola de la lista
```

```prolog
?- list_member(b, [a, b, c]).
true.
?- list_member(b, [a, [b, c]]).
false.
?- list_member([b, c], [a, [b, c]]).
true.
```

##### 10.1.2. Cálculo de longitud

La longitud de una lista se puede calcular utilizando las siguientes reglas:

```prolog
% list_basics.pl
list_length([], 0). % La longitud de una lista vacía es 0
list_length([_|Tail], Length) :- list_length(Tail, Length1), Length is Length1 + 1.
```

```prolog
?- list_length([a, b, c, d, e, f, g, h, i, j], Len).
Len = 10.
?- list_length([], Len).
Len = 0.
?- list_length([[a, b], [c, d], [e, f]], Len).
Len = 3.
```

##### 10.1.3. Concatenación

La concatenación de listas se puede realizar utilizando las siguientes reglas:

```prolog
% list_basics.pl
list_concat([], L, L). % Concatenar una lista vacía con otra lista
list_concat([H|T], L, [H|R]) :- list_concat(T, L, R). % Concatenar dos listas
```

```prolog
?- list_concat([1, 2], [a, b, c], NewList).
NewList = [1, 2, a, b, c].
?- list_concat([], [a, b, c], NewList).
NewList = [a, b, c].
?- list_concat([[1, 2, 3], [p, q, r]], [a, b, c], NewList).
NewList = [[1, 2, 3], [p, q, r], a, b, c].
```

##### 10.1.4. Borrar elemento de una lista

La eliminación de un elemento de una lista se puede realizar utilizando las siguientes reglas:

```prolog
% list_basics.pl
list_delete(X, [X], []). % Eliminar un elemento de una lista
list_delete(X, [X|Tail], Tail). % Eliminar un elemento de la cabeza de la lista
list_delete(X, [Y|Tail], [Y|NewTail]) :- list_delete(X, Tail, NewTail). % Eliminar un elemento de la cola de la lista
```

```prolog
?- list_delete(a, [a, e, i, o, u], NewList).
NewList = [e, i, o, u] .
?- list_delete(a, [a], NewList).
NewList = [] .
?- list_delete(X, [a, e, i, o, u], [a, e, o, u]) .
X = i .
```

##### 10.1.5. Agregar elemento a una lista

La adición de un elemento a una lista se puede realizar utilizando las siguientes reglas:

```prolog
% list_basics.pl
list_append(A, T, T) :- list_member(A, T), !. % Agregar un elemento a una lista
list_append(A, T, [A|T]). % Agregar un elemento a la cabeza de la lista
```

```prolog
?- list_append(a, [e, i, o, u], NewList).
NewList = [a, e, i, o, u].
?- list_append(e, [e, i, o, u], NewList).
NewList = [e, i, o, u].
?- list_append([a, b], [e, i, o, u], NewList).
NewList = [[a, b], e, i, o, u].
```

##### 10.1.6. Insertar elemento en una lista

```prolog
% list_basics.pl
list_insert(X, L, R) :- list_delete(X, R, L). % Insertar un elemento en una lista
```

```prolog
?- list_insert(a, [e, i, o, u], NewList).
NewList = [a, e, i, o, u].
```

##### 10.1.7 Muchas otras operaciones

Existen muchas otras operaciones que se pueden realizar con listas en Prolog, como la inversión de listas, la búsqueda de elementos, la eliminación de duplicados, etc. Estas operaciones son fundamentales para trabajar con datos en Prolog y se pueden implementar utilizando reglas y predicados.

### 11. Recursión y estructuras

En esta sección se explorará la recursión y las estructuras en Prolog.

#### 11.1. Recursión

La recursión es una técnica fundamental en Prolog. Permite definir predicados en términos de sí mismos, lo que permite resolver problemas complejos de manera elegante y concisa.

```prolog
is_digesting(X, Y) :- just_ate(X, Y).
is_digesting(X, Y) :- just_ate(X, Z), is_digesting(Z, Y).
```

En este ejemplo, el predicado `is_digesting/2` se define en términos de sí mismo. Esto significa que Prolog puede seguir llamando a `is_digesting/2` hasta que llegue a un caso base.

#### 11.2. Estructuras

Las estructuras son una forma de agrupar datos relacionados en Prolog. Algunos ejemplos de estructuras son:

```prolog
% Estructuras
point(1, 1).
point(2, 3).
seg(point(1, 1), point(2, 3)).
triangle(point(4, Z), point(6, 4), point(7, 1)).
```

Las estructuras se pueden utilizar para representar datos complejos y se pueden combinar con reglas y predicados para realizar operaciones sobre esos datos.

```prolog
?- point(X, Y).
X = Y, Y = 1 ;
X = 2,
Y = 3.
?- seg(X, Y).
X = point(1, 1),
Y = point(2, 3).
?- triangle(X, Y, Z).
X = point(4, _),
Y = point(6, 4),
Z = point(7, 1).
```

### 12. Retroceso

El retroceso es una característica fundamental de Prolog. Permite a Prolog explorar múltiples soluciones a un problema y volver atrás cuando no se encuentra una solución.

El retroceso se produce automáticamente cuando Prolog no puede encontrar una solución a una consulta. En este caso, Prolog vuelve al último punto de decisión y prueba una alternativa.

Podemos usar `trace.` para habilitar el seguimiento de la ejecución de Prolog y ver cómo se produce el retroceso. Para habilitar el seguimiento, simplemente escribe `trace.` en la consola de Prolog.

```prolog
?- trace.
```

Esto habilitará el seguimiento y mostrará información detallada sobre la ejecución de Prolog. Puedes usar `notrace.` para deshabilitar el seguimiento.

### 13. Diferente y negación

Podemos definir el predicado `different/2` para verificar si dos argumentos son diferentes. Esto se puede hacer utilizando la siguiente regla:

```prolog
% diff_rel.pl
different(X, X) :- !, fail. % Si X y Y son iguales, falla
different(X, Y). % Si X y Y son diferentes, tiene éxito
```

Esto significa que si `X` y `Y` son iguales, el predicado `different/2` fallará. Si son diferentes, el predicado tendrá éxito. Con esto, podemos verificar si dos elementos son diferentes.

```prolog
?- different(100, 200).
true.
?- different(100, 100).
false.
?- different(abc, def).
true.
?- different(abc, abc).
false.
```

También podemos definir el predicado `not/1` para verificar si un predicado es falso. Esto se puede hacer utilizando la siguiente regla:

```prolog
% not_rel.pl
not(P) :- P, !, fail ; true. % Si P es verdadero, falla; de lo contrario, tiene éxito
```

Esto significa que si `P` es verdadero, el predicado `not/1` fallará. Si `P` es falso, el predicado tendrá éxito.

```prolog
?- not(true).
false.
?- not(false).
true.
```

### 14. Entradas y salidas

Prolog permite realizar operaciones de entrada y salida utilizando los predicados `write/1`, `read/1`, `nl/0`, `tab/1`, entre otros.

- `write(X)`: Escribe el valor de `X` en la salida estándar.
- `read(X)`: Lee un valor de la entrada estándar y lo unifica con `X`.
- `nl`: Imprime una nueva línea.
- `tab(N)`: Imprime `N` espacios en blanco.

### 15. Predicados predefinidos

Prolog tiene varios predicados predefinidos que se pueden utilizar para realizar operaciones comunes. Algunos de los más utilizados son:

- `var(X)`: Verifica si `X` es una variable.
- `novar(X)`: Verifica si `X` no es una variable.
- `atom(X)`: Verifica si `X` es un átomo.
- `number(X)`: Verifica si `X` es un número.
- `integer(X)`: Verifica si `X` es un número entero.
- `float(X)`: Verifica si `X` es un número de punto flotante.
- `atomic(X)`: Verifica si `X` es un átomo o un número.
- `compound(X)`: Verifica si `X` es una estructura.
- `ground(X)`: Verifica si `X` es un término completamente instanciado.

### 16. Estructura de árbol (caso de estudio)

Por último, vamos a implementar un árbol en Prolog. Un árbol es una estructura de datos jerárquica que consiste en nodos conectados por aristas. Cada nodo puede tener cero o más hijos, y cada nodo tiene un padre, excepto la raíz.

Vamos a crear un archivo llamado `case_tree.pl` y escribir el siguiente código:

```prolog
% case_tree.pl
:- op(500, xfx, is_parent).
a is_parent b. c is_parent g. f is_parent l. j is_parent q.
a is_parent c. c is_parent h. f is_parent m. j is_parent r.
a is_parent d. c is_parent i. h is_parent n. j is_parent s.
b is_parent e. d is_parent j. i is_parent o. m is_parent t.
b is_parent f. e is_parent k. i is_parent p. n is_parent u.
n is_parent v.

:- op(500, xfx, is_sibling_of).
X is_sibling_of Y :- Z is_parent(X), Z is_parent(Y), X \== Y.

leaf_node(Node) :- \+ is_parent(Node, Child).

:- op(500, xfx, is_at_same_level).

X is_at_same_level X .
X is_at_same_level Y :- W is_parent X, Z is_parent Y, W is_at_same_level Z.
```

Finalmente, podemos cargar el archivo en Prolog y hacer consultas sobre el árbol:

```prolog
?- [case_tree].
true.
?- i is_parent p.
true.
?- i is_parent s.
false.
?- is_parent(i,p).
true.
?- e is_sibling_of f.
true.
?- is_sibling_of(e,g).
false.
?- leaf_node(v).
true.
?- leaf_node(a).
false.
?- is_at_same_level(l,s).
true.
?- l is_at_same_level v.
false.
```

[Regresar al inicio](#tabla-de-contenido)
