---
title: "Práctica 4: Prolog"
description: "Instalación del entorno SWI-Prolog, fundamentos del paradigma lógico, hechos, reglas, consultas, recursión, listas, operadores, predicados integrados y aplicaciones avanzadas."
date: 2025-10-22
image: https://images.unsplash.com/photo-1519389950473-47ba0277781c?w=1200
categories:
  - Programación
  - Paradigmas
tags:
  - prolog
  - paradigma-logico
  - hechos
  - reglas
  - consultas
  - recursion
  - listas
  - swi-prolog
slug: practica-4
type: "post"

---




                               
                               
                               
                                             UABC
                            PARADIGMAS DE LA PROGRAMACIÓN
                                        PRÁCTICA #4
                            FERNANDA ITZEL FLORES VALENZUELA
                                          376160
                                        Grupo 941 

---

## 1. Introducción

Durante el desarrollo de esta práctica, exploré el paradigma lógico, que representa una forma completamente distinta de pensar en la programación. A diferencia de los paradigmas que ya conocía (como el imperativo o el orientado a objetos), donde le decimos a la computadora exactamente qué pasos seguir, aquí simplemente describimos las relaciones que existen entre diferentes elementos y dejamos que el sistema encuentre las respuestas por sí mismo.

Trabajé principalmente con Prolog, que es el lenguaje más conocido de este paradigma. Lo interesante es que Prolog no ejecuta instrucciones secuencialmente, sino que trabaja con una base de conocimiento donde almacenamos información y luego hacemos consultas sobre ella. El sistema se encarga de buscar las respuestas usando un proceso llamado inferencia lógica.

Este paradigma es particularmente útil en áreas como:
- Desarrollo de sistemas expertos que simulan el conocimiento humano
- Análisis y procesamiento de lenguaje natural
- Problemas de inteligencia artificial que requieren razonamiento
- Situaciones donde necesitamos buscar entre múltiples posibilidades

La diferencia fundamental que observé es que en lugar de escribir "cómo hacer algo", escribo "qué es verdad" y Prolog se encarga del resto.

---

## 2. Preparación del Ambiente de Trabajo

Para comenzar a trabajar con Prolog, instalé SWI-Prolog siguiendo estos pasos:

### Proceso de instalación:

1. Ingresé al sitio web oficial de [SWI-Prolog](https://www.swi-prolog.org/)
2. En la página principal, busqué la opción de descargas
3. Seleccioné la versión estable más reciente (Stable release)
4. Elegí la versión compatible con mi sistema operativo
5. Acepté los términos de uso
6. Descargué el instalador y procedí con la instalación estándar

Una vez completada la instalación, pude acceder al entorno de diferentes maneras:
- A través de la consola interactiva donde puedo probar comandos directamente
- Creando archivos con extensión `.pl` donde guardo mi código
- Usando el editor integrado que trae SWI-Prolog

---

## 3. Fundamentos de la Programación Lógica

### 3.1 Los Hechos: La Base del Conocimiento

Los hechos son la forma más simple de expresar información en Prolog. Representan verdades absolutas sobre nuestro dominio de conocimiento.

**La estructura básica que aprendí es:**
```prolog
predicado(argumentos).
```

**Aspectos importantes que debo recordar:**
- Todo comienza con minúscula
- Siempre termina con un punto
- Puedo usar comillas para textos con espacios o mayúsculas

**Ejemplos que implementé:**
```prolog
bird(luna).
likes_coffee(maria, espresso).
color_of(sky, blue).
enjoys_reading(carlos).
student(ana).
```

Cada uno de estos hechos declara algo que es cierto en mi base de conocimiento: Luna es un pájaro, María le gusta el café espresso, etc.

### 3.2 Las Reglas: Definiendo Relaciones Complejas

Las reglas me permiten expresar conocimiento condicional. Son como decir "esto es verdad si aquello también lo es".

**El formato que uso es:**
```prolog
conclusion :- condiciones.
```

Esto se lee como: "La conclusión es verdadera SI las condiciones se cumplen"

**Ejemplos prácticos:**
```prolog
energetic(luna) :- flies(luna).
tired(carlos) :- works_late(carlos).
can_collaborate(ana, luis) :- studies_cs(ana), studies_cs(luis).
can_travel(sofia) :- has_passport(sofia), has_time(sofia).
```

**Descubrí dos conectores importantes:**
- La coma (`,`) funciona como "Y" - todas las condiciones deben cumplirse
- El punto y coma (`;`) funciona como "O" - al menos una condición debe cumplirse

### 3.3 Haciendo Preguntas: Las Consultas

Una vez que tengo mi base de conocimiento, puedo hacer preguntas. Esto es lo que hace a Prolog realmente poderoso.

**Ejemplos de consultas:**
```prolog
?- bird(luna).
true.

?- energetic(carlos).
false.

?- student(X).
X = ana ;
X = luis.
```

Prolog puede responder de tres formas:
- Confirmando si algo es verdadero o falso
- Encontrando valores que hacen verdadera una relación
- Mostrando múltiples respuestas posibles (usando `;` para ver la siguiente)

---

## 4. Construyendo Bases de Conocimiento

Durante la práctica, construí varias bases de conocimiento de complejidad creciente:

### Primera base: Información sobre estudiantes
```prolog
student(ana).
student(luis).
student(carmen).
knows_programming(ana).
```

Esta es la más simple, solo declara hechos directos.

### Segunda base: Relacionando hobbies con personalidad
```prolog
plays_guitar(diego).
creative(X) :- plays_guitar(X).
creative(X) :- paints(X).
```

Aquí empecé a usar reglas: alguien es creativo si toca guitarra o si pinta.

### Tercera base: Preferencias basadas en intereses
```prolog
admires(sofia, X) :- loves_science(X).
```

Sofía admira a las personas que aman la ciencia.

### Cuarta base: Relaciones de trabajo básicas
```prolog
works_at(alberto, acme_corp).
works_at(beatriz, acme_corp).
position(alberto, developer).
position(beatriz, developer).

colleague(X, Y) :- 
    works_at(Z, X), 
    works_at(Z, Y), 
    position(X, developer), 
    position(Y, developer),
    X \== Y.
```

**Un detalle importante que descubrí:** Necesito usar `X \== Y` para evitar que el sistema diga que alguien es colega de sí mismo. Sin esta condición, cuando pregunto "¿quién es colega de Alberto?", Prolog incluiría a Alberto en la respuesta, lo cual no tiene sentido.

---

## 5. Proyecto: Sistema de Árbol Genealógico

Uno de los ejercicios más interesantes fue crear un sistema completo de relaciones familiares. Lo desarrollé en etapas:

### 5.1 Definiendo la familia (family.pl)

Primero declaré todos los miembros de la familia:

```prolog
% Identifico quiénes son mujeres
female(maria).
female(elena).
female(sofia).
female(lucia).

% Identifico quiénes son hombres
male(juan).
male(carlos).
male(diego).
male(pablo).

% Establezco las relaciones padre-hijo
parent(maria, carlos).
parent(diego, carlos).
parent(diego, elena).
parent(carlos, lucia).
parent(carlos, sofia).
parent(sofia, juan).
parent(pablo, juan).
```

### 5.2 Definiendo relaciones directas

Con los hechos básicos, creé reglas para relaciones más específicas:

```prolog
% Una madre es un padre que además es mujer
mother(X, Y) :- parent(X, Y), female(X).

% Un padre es un padre que además es hombre
father(X, Y) :- parent(X, Y), male(X).

% Alguien tiene hijos si es padre de alguien
has_children(X) :- parent(X, _).

% Hermanas: comparten al menos un padre, son diferentes y son mujeres
sister(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    female(X), 
    X \== Y.

% Hermanos: comparten al menos un padre, son diferentes y son hombres
brother(X, Y) :- 
    parent(Z, X), 
    parent(Z, Y), 
    male(X), 
    X \== Y.
```

### 5.3 Expandiendo las relaciones (family_ext.pl)

Después agregué relaciones más complejas:

```prolog
% Los abuelos son padres de los padres
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).

% Una esposa comparte hijos con un hombre
spouse(X, Y) :- 
    parent(X, Z), 
    parent(Y, Z), 
    female(X), 
    male(Y).

% Una tía es hermana de uno de tus padres
aunt(X, Z) :- sister(X, Y), parent(Y, Z).
```

### 5.4 Usando recursión para ancestros (family_rec.pl)

La parte más desafiante fue implementar el concepto de "ancestro":

```prolog
% Caso simple: tu padre es tu ancestro directo
ancestor(X, Z) :- parent(X, Z).

% Caso complejo: X es ancestro de Z si X es padre de alguien 
% que a su vez es ancestro de Z
ancestor(X, Z) :- 
    parent(X, Y), 
    ancestor(Y, Z).
```

**Lo que hace especial esta regla:** Puede encontrar bisabuelos, tatarabuelos, o cualquier ancestro sin importar qué tan lejos esté en el árbol familiar. Prolog sigue buscando hacia atrás hasta encontrar todas las conexiones.

---

## 6. Trabajando con Diferentes Tipos de Datos

Aprendí que Prolog maneja varios tipos de información:

### Átomos
Son como nombres o etiquetas. Ejemplos:
- `luna`, `universidad`, `prolog`
- `'María José'` (con comillas para mayúsculas o espacios)
- `'Buenos Aires'`

### Variables
Siempre empiezan con mayúscula:
- `X`, `Y`, `Persona`, `Total`
- `_` para cuando no me importa el valor
- `_Aux` para variables auxiliares

### Números
Puedo usar enteros y decimales:
- Enteros: `250`, `-89`, `2024`
- Decimales: `9.81`, `1500.50`, `-3.14`

### Estructuras complejas
Puedo crear datos más elaborados:
```prolog
fecha(15, marzo, 2024).
coordenada(45, 90).
estudiante(nombre('Ana'), edad(20), carrera('Ingeniería')).
```

---

## 7. Operaciones y Comparaciones

### 7.1 Comparando valores

Prolog ofrece varios operadores:

```prolog
>    % Mayor que
<    % Menor que
>=   % Mayor o igual
=<   % Menor o igual (cuidado: no es <=)
=:=  % Compara valores numéricos
=\=  % Diferentes numéricamente
==   % Exactamente igual
\==  % Exactamente diferente
```

### 7.2 Haciendo cálculos

Para operaciones matemáticas uso `is`:

```prolog
+    % Sumar
-    % Restar
*    % Multiplicar
/    % Dividir (resultado real)
//   % Dividir (resultado entero)
mod  % Obtener el resto
**   % Elevar a una potencia
```

**Ejemplos prácticos:**
```prolog
?- X is 250 + 150.
X = 400.

?- Y is 3 ** 4.
Y = 81.

?- Z is 23 mod 7.
Z = 2.
```

**Una regla que compara números:**
```prolog
compare_values(X, Y) :- 
    X >= Y, 
    write('El primer valor es mayor o igual').
    
compare_values(X, Y) :- 
    X < Y, 
    write('El primer valor es menor').
```

---

## 8. Control de Flujo en Prolog

### 8.1 Conteo recursivo

Implementé un contador que muestra números del 1 al 15:

```prolog
% Cuando llego a 15, me detengo
count_to_15(15) :- 
    write(15), 
    nl.

% Para cualquier otro número, lo muestro y continúo con el siguiente
count_to_15(X) :- 
    write(X), 
    nl, 
    Y is X + 1, 
    count_to_15(Y).
```

**Para usarlo:**
```prolog
?- count_to_15(1).
1
2
3
...
15
true.
```

### 8.2 Generando rangos

El predicado `between/3` es muy útil:

```prolog
display_range(Start, End) :-
    between(Start, End, Value),
    write(Value), nl,
    fail.
display_range(_, _).
```

### 8.3 Decisiones condicionales

Prolog tiene una estructura if-then-else:

```prolog
maximum(X, Y, Max) :-
    (X >= Y -> Max = X ; Max = Y).
```

Se lee: "Si X es mayor o igual a Y, entonces Max es X; si no, Max es Y"

---

## 9. Listas: Una Estructura Fundamental

### 9.1 ¿Qué son las listas?

Las listas son colecciones ordenadas de elementos. Se representan entre corchetes:

```prolog
[azul, amarillo, verde]    % Lista de colores
[]                          % Lista vacía
[10, 20, 30, 40]           % Lista de números
[perro, gato, conejo]      % Lista de animales
```

**Una característica especial:** Puedo separar el primer elemento del resto:
```prolog
[Primero | Resto]
[perro | [gato, conejo]]    % Es lo mismo que [perro, gato, conejo]
```

### 9.2 Operaciones básicas que implementé

**Verificar si un elemento está en la lista:**
```prolog
% Si X es la cabeza, está en la lista
member_of(X, [X|_]).

% Si no, busco en el resto de la lista
member_of(X, [_|Tail]) :- member_of(X, Tail).
```

**Calcular la longitud:**
```prolog
% Una lista vacía tiene longitud 0
length_of([], 0).

% Para cualquier otra lista, cuento 1 más que la cola
length_of([_|Tail], Length) :- 
    length_of(Tail, TailLen), 
    Length is TailLen + 1.
```

**Unir dos listas:**
```prolog
% Unir con lista vacía da la segunda lista
concatenate([], L, L).

% Tomo el primer elemento de la primera lista y lo pongo al inicio
concatenate([X|L1], L2, [X|L3]) :- concatenate(L1, L2, L3).
```

**Agregar al inicio:**
```prolog
add_front(Element, List, [Element|List]).
```

**Eliminar un elemento:**
```prolog
% Si es el primero, devuelvo el resto
remove_item(X, [X|Tail], Tail).

% Si no, lo busco en el resto
remove_item(X, [Y|Tail], [Y|Rest]) :- remove_item(X, Tail, Rest).
```

### 9.3 Operaciones avanzadas

**Invertir una lista:**
```prolog
reverse_list([], []).
reverse_list([Head|Tail], Reversed) :- 
    reverse_list(Tail, RevTail), 
    append_end(RevTail, Head, Reversed).

append_end([], Item, [Item]).
append_end([H|T], Item, [H|Result]) :- append_end(T, Item, Result).
```

**Generar permutaciones:**
```prolog
permute([], []).
permute(List, [X|Perm]) :- 
    remove_item(X, List, Rest), 
    permute(Rest, Perm).
```

**Sumar todos los elementos:**
```prolog
sum_list([], 0).
sum_list([Head|Tail], Sum) :- 
    sum_list(Tail, TailSum), 
    Sum is Head + TailSum.
```

**Encontrar el máximo:**
```prolog
max_in_list([X], X).
max_in_list([Head|Tail], Max) :- 
    max_in_list(Tail, TailMax), 
    (Head > TailMax -> Max = Head ; Max = TailMax).
```

**Dividir una lista en dos:**
```prolog
split_in_half([], [], []).
split_in_half([X], [X], []).
split_in_half([X, Y|Tail], [X|L1], [Y|L2]) :- 
    split_in_half(Tail, L1, L2).
```

**Filtrar números pares:**
```prolog
even_numbers([], []).
even_numbers([H|T], [H|Result]) :- 
    0 is H mod 2, 
    even_numbers(T, Result).
even_numbers([H|T], Result) :- 
    1 is H mod 2, 
    even_numbers(T, Result).
```

---

## 10. Predicados del Sistema

Prolog incluye funciones útiles que puedo usar directamente:

### Verificación de tipos
```prolog
var(X)        % ¿Es una variable sin valor?
atom(X)       % ¿Es un átomo?
number(X)     % ¿Es un número?
compound(X)   % ¿Es una estructura compuesta?
integer(X)    % ¿Es un entero?
float(X)      % ¿Es un decimal?
```

### Funciones matemáticas
```prolog
random(Min, Max, X)    % Genera un número aleatorio
between(Min, Max, X)   % Genera números en un rango
abs(X)                 % Valor absoluto
sqrt(X)                % Raíz cuadrada
max(X, Y)              % El mayor de dos números
min(X, Y)              % El menor de dos números
sin(X)                 % Seno
cos(X)                 % Coseno
exp(X)                 % e elevado a X
log(X)                 % Logaritmo natural
```

---

## 11. El Mecanismo de Backtracking

Una de las características más poderosas que descubrí en Prolog es el backtracking. Es la capacidad del sistema de explorar automáticamente diferentes posibilidades.

**Un ejemplo simple:**
```prolog
fruit(manzana).
fruit(naranja).
fruit(pera).

?- fruit(X).
X = manzana ;
X = naranja ;
X = pera.
```

**Cómo funciona:**
1. Prolog encuentra la primera solución (manzana)
2. Si presiono `;`, vuelve atrás y busca otra opción (naranja)
3. Continúa así hasta que no hay más opciones (pera)
4. Finalmente dice `false` si no hay más

**Controlando el backtracking con el "corte" (!):**
```prolog
first_fruit(X) :- fruit(X), !.

?- first_fruit(X).
X = manzana.  % Solo da una respuesta y se detiene
```

El símbolo `!` le dice a Prolog "no busques más alternativas aquí".

---

## 12. Problemas Clásicos Resueltos

### 12.1 Torres de Hanoi

Este problema consiste en mover discos entre tres postes siguiendo reglas específicas:

```prolog
% Mover un solo disco es directo
move_disk(1, Source, Target, _) :- 
    write('Mover disco de '), 
    write(Source), 
    write(' hacia '), 
    write(Target), 
    nl.

% Para mover N discos:
% 1. Muevo N-1 discos al auxiliar
% 2. Muevo el disco grande al destino
% 3. Muevo los N-1 discos del auxiliar al destino
move_disk(N, Source, Target, Auxiliary) :- 
    N > 1, 
    M is N - 1, 
    move_disk(M, Source, Auxiliary, Target), 
    move_disk(1, Source, Target, _), 
    move_disk(M, Auxiliary, Target, Source).
```

### 12.2 Factorial recursivo

```prolog
factorial(0, 1).
factorial(N, Result) :-
    N > 0,
    N1 is N - 1,
    factorial(N1, Result1),
    Result is N * Result1.
```

### 12.3 Fibonacci

```prolog
fibonacci(0, 0).
fibonacci(1, 1).
fibonacci(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fibonacci(N1, F1),
    fibonacci(N2, F2),
    Result is F1 + F2.
```

### 12.4 Otros problemas explorados

Durante la práctica también trabajé con:
- **Sistema de recomendaciones:** Sugerir productos basados en preferencias
- **Planificación de horarios:** Asignar clases sin conflictos
- **Árboles binarios:** Implementación de inserción, búsqueda y recorridos
- **Problemas de lógica:** Acertijos como "quién vive dónde"

---

## 13. Reflexiones Finales

Después de completar esta práctica, puedo decir que el paradigma lógico me ofreció una perspectiva completamente nueva sobre la programación. Algunos puntos clave que aprendí:

**Cambio de mentalidad:**
En lugar de pensar en "pasos a seguir", aprendí a pensar en "relaciones que existen". Es como cambiar de dar instrucciones a describir un mundo y dejar que el sistema encuentre las respuestas.

**El poder de la declaración:**
No necesito explicar cómo encontrar algo, solo necesito describir qué estoy buscando. Prolog se encarga de la búsqueda automáticamente.

**Recursión natural:**
Muchos problemas que parecían complicados se volvieron más simples al expresarlos de forma recursiva. La recursión en Prolog se siente más intuitiva que en otros lenguajes.

**Backtracking automático:**
La capacidad de explorar automáticamente múltiples soluciones es increíblemente poderosa para problemas donde hay varias respuestas posibles.

**Aplicaciones prácticas:**
Aunque inicialmente pensé que Prolog era puramente académico, descubrí que es muy útil para:
- Sistemas que necesitan razonar sobre información
- Aplicaciones que trabajan con conocimiento estructurado
- Problemas de optimización y búsqueda
- Análisis de relaciones complejas

**Desafíos encontrados:**
- Al principio me costó dejar de pensar en "cómo hacer" las cosas
- Entender el orden de evaluación y el backtracking requirió práctica
- Depurar programas lógicos es diferente a lenguajes imperativos

Esta práctica me dio las herramientas fundamentales para trabajar con programación lógica y me mostró que hay múltiples formas de abordar los problemas computacionales. Cada paradigma tiene su lugar y sus fortalezas.

---

## Referencias

- Gallegos Mariscal, J.C. (2025). Unidad V: El paradigma lógico. Material del curso Paradigmas de la Programación.
- Ejemplos y ejercicios desarrollados durante las sesiones de clase

[Repositorio](https://github.com/pinapinv/portafolioPP.git)