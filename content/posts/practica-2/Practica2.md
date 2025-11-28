---
title: "Práctica 2: Programación Orientada a Objetos"
description: "Migración de sistema de biblioteca de C a Python aplicando conceptos de POO: clases, objetos, encapsulamiento, abstracción, herencia y polimorfismo"
date: 2025-10-01
image: https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800
categories:
  - Programación
  - Paradigmas
tags:
  - python
  - poo
  - orientado-a-objetos
  - clases
  - herencia
  - polimorfismo
  - encapsulamiento
slug: practica-2
type: "post"
---

# Contenido de la práctica

                                         UABC
                            PARADIGMAS DE LA PROGRAMACIÓN
                                        PRÁCTICA #2
                            FERNANDA ITZEL FLORES VALENZUELA
                                          376160
                                        Grupo 941 


Introducción:
En esta práctica se realizará la migración del sistema de gestión de biblioteca desarrollado en C hacia Python, aplicando el paradigma de Programación Orientada a Objetos (POO). Este ejercicio permitirá comprender las diferencias entre la programación estructurada y la orientada a objetos, así como identificar las ventajas que ofrece POO en términos de organización, mantenibilidad y reutilización del código.


Desarrollo:


1. Conceptos de Programación Orientada a Objetos

1.1 Clase

Una clase es una plantilla o molde que define las características (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella.

Ejemplo en el código:

    class Item:
        def __init__(self, id, titulo, autor=None):
            self._id = id
            self._titulo = titulo
            self._autor = autor
            self._disponible = True

La clase Item define la estructura base para todos los ítems de la biblioteca.

1.2 Objeto

Un objeto es una instancia específica de una clase. Es una entidad concreta que tiene valores específicos para los atributos definidos en la clase.

Ejemplo en el código:

    libro1 = Libro(1, "Cien Años de Soledad", "Gabriel García Márquez", 1967, "Ficción")
    revista1 = Revista(2, "National Geographic", "Varios", 2024, 150)

Aquí libro1 y revista1 son objetos (instancias) de las clases Libro y Revista respectivamente.

1.3 Herencia

La herencia permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos. Esto promueve la reutilización del código.

Ejemplo en el código:

    class Libro(Item):
        def __init__(self, id, titulo, autor, año_publicacion, genero):
            super().__init__(id, titulo, autor)
            self._año_publicacion = año_publicacion
            self._genero = genero

    class Revista(Item):
        def __init__(self, id, titulo, autor, año, numero_edicion):
            super().__init__(id, titulo, autor)
            self._año = año
            self._numero_edicion = numero_edicion

Tanto Libro como Revista heredan de Item, obteniendo sus atributos y métodos base, pero agregando características específicas.

# 1.4 Encapsulamiento

El encapsulamiento oculta los detalles internos de implementación y expone solo lo necesario mediante métodos públicos. En Python se utiliza el prefijo _ para indicar atributos privados.

Ejemplo en el código:

    class Usuario:
        def __init__(self, id, nombre):
            self._id = id  # Atributo privado
            self._nombre = nombre  # Atributo privado
            self._items_prestados = []
        
        def get_id(self):  # Método público para acceder al atributo
            return self._id
        
        def get_nombre(self):
            return self._nombre

Los atributos _id y _nombre no se acceden directamente, sino a través de métodos getter.

# 1.5 Abstracción

La abstracción consiste en mostrar solo la información relevante y ocultar los detalles complejos de implementación. Se enfoca en "qué hace" más que en "cómo lo hace".

Ejemplo en el código:

    class Biblioteca:
        def prestar_item(self, usuario_id, item_id):
            usuario = self._buscar_usuario(usuario_id)
            item = self._buscar_item(item_id)
            
            if usuario and item and item.esta_disponible():
                item.prestar()
                usuario.prestar_item(item_id)
                return True
            return False

El método prestar_item() abstrae toda la lógica de préstamo. El usuario de la clase no necesita conocer los detalles internos.

# 1.6 Polimorfismo

El polimorfismo permite que diferentes clases respondan de manera distinta al mismo método. Cada clase hija puede sobrescribir métodos de la clase padre.

Ejemplo en el código:

    class Item:
        def mostrar_info(self):
            pass  # Método que será sobrescrito

    class Libro(Item):
        def mostrar_info(self):
            return f"Libro: {self._titulo} por {self._autor} ({self._año_publicacion})"

    class Revista(Item):
        def mostrar_info(self):
            return f"Revista: {self._titulo} - Edición #{self._numero_edicion} ({self._año})"

El método mostrar_info() se comporta diferente según el tipo de objeto (Libro o Revista).

2. Comparación entre la versión en C y la versión en Python

Organización de datos: En C se usaban estructuras (struct) separadas de las funciones, mientras que en Python las clases encapsulan datos y métodos juntos.

Gestión de memoria: En C la gestión es manual mediante malloc, free y realloc. En Python es automática gracias al garbage collector.

Reutilización de código: En C se logra mediante funciones genéricas, mientras que en Python se utiliza herencia y composición.

Extensibilidad: En C requiere modificar múltiples funciones para agregar nuevos tipos. En Python se pueden agregar nuevas clases sin modificar las existentes.

Mantenimiento: El código en C es más complejo de mantener cuando crece, mientras que Python es más modular y fácil de mantener.

Abstracción: En C la abstracción es limitada y basada en funciones, en Python es natural mediante clases e interfaces.

Ejemplo concreto:

En C, agregar un nuevo tipo de ítem como DVD requeriría modificar o duplicar múltiples funciones (addBook, displayBooks, etc.), gestionar manualmente la memoria adicional y actualizar estructuras de datos existentes.

En Python con POO solo se crea una nueva clase que hereda de Item:

    class DVD(Item):
        def __init__(self, id, titulo, director, duracion):
            super().__init__(id, titulo, director)
            self._duracion = duracion
        
        def mostrar_info(self):
            return f"DVD: {self._titulo} - Director: {self._autor} ({self._duracion} min)"

No se necesita modificar código existente.

3. Implementación en Python

El código completo incluye las siguientes clases principales:

Item: Clase base abstracta para todos los ítems de la biblioteca.

Libro: Clase derivada que representa libros con atributos como año de publicación y género.

Revista: Clase derivada que representa revistas con atributos como número de edición.

Usuario: Representa a los miembros de la biblioteca y maneja los ítems prestados.

Biblioteca: Gestiona todo el sistema incluyendo agregar ítems, usuarios, realizar préstamos y devoluciones.

La persistencia se implementó usando JSON para guardar y cargar datos. El menú interactivo permite realizar todas las operaciones del sistema original de manera intuitiva.


Conclusiones:
La migración del sistema de biblioteca de C a Python con POO demostró varias ventajas importantes. El código POO es más intuitivo y refleja mejor el modelo del mundo real, ya que las entidades como libros, usuarios y biblioteca se representan naturalmente como objetos. Los cambios se realizan en clases específicas sin afectar el resto del sistema, lo cual reduce el riesgo de errores. La herencia permite compartir código común entre clases similares, como Libro y Revista que heredan de Item. Agregar nuevas funcionalidades o tipos de ítems es sencillo mediante la creación de nuevas clases. Los detalles internos quedan ocultos exponiendo solo interfaces simples para interactuar con los objetos. Python elimina la complejidad de gestionar memoria manualmente, reduciendo errores y simplificando el código. La POO demuestra ser especialmente útil en sistemas que modelan entidades del mundo real con comportamientos complejos como este sistema de biblioteca.

Repositorio https://github.com/pinapinv/portafolioPP