+++
date = '2025-05-04T08:45:55-07:00'
draft = false
title = 'Práctica 2'
+++

## Tabla de contenido

- [Elementos fundamentales de los lenguajes de programación](#elementos-fundamentales-de-los-lenguajes-de-programación)
  - [1. Nombres](#1-nombres)
  - [2. Objetos](#2-objetos)
  - [3. Entornos](#3-entornos)
    - [3.1. Global](#31-global)
    - [3.2. Locales](#32-locales)
    - [3.3. No locales](#33-no-locales)
  - [4. Bloques](#4-bloques)
  - [5. Alcance](#5-alcance)
    - [5.1. Bloques en línea anidados](#51-bloques-en-línea-anidados)
    - [5.2. Alcance en funciones](#52-alcance-en-funciones)
  - [6. Administración de memoria](#6-administración-de-memoria)
    - [6.1. Almacenamiento estático](#61-almacenamiento-estático)
    - [6.2. Almacenamiento automático](#62-almacenamiento-automático)
    - [6.3. Almacenamiento de hilo local o subproceso](#63-almacenamiento-de-hilo-local-o-subproceso)
    - [6.4. Almacenamiento dinámico](#64-almacenamiento-dinámico)
  - [7. Expresiones](#7-expresiones)
  - [8. Comandos](#8-comandos)
  - [9. Secuencia](#9-secuencia)
    - [9.1. Selección](#91-selección)
    - [9.2. Iteración](#92-iteración)
    - [9.3. Recursión](#93-recursión)
    - [9.4. Subprogramas](#94-subprogramas)
  - [10. Tipos de datos](#10-tipos-de-datos)

## Elementos fundamentales de los lenguajes de programación

Aquí está el [repositorio](https://github.com/World-X/paradigmas-portafolio) y el [sitio web](https://world-x.github.io/paradigmas-portafolio/).

### 1. Nombres

Algunos nombres (identificadores) son: `library`, `choice`, `book_id`, `title`, `author`, `genre`, `publication_year`, `quantity`, `is_digital`.

```py
# biblioteca.py:254
library = Library()
```

```py
# biblioteca.py:268
choice = int(input("Indica tu opcion: "))
```

```py
# biblioteca.py:271-277
book_id = int(input("Ingresa ID del libro: "))
title = input("Ingresa titulo del libro: ")
author = input("Ingresa nombre del autor: ")
publication_year = int(input("Ingresa el ano de publicacion: "))
genre = input("Ingresa el genero del libro: ")
quantity = int(input("Ingresa la cantidad de libros: "))
is_digital = input("Es un libro digital? (s/n): ").lower() == 's'
```

### 2. Objetos

Existen en total 5 clases: `Genre`, `Book`, `DigitalBook`, `Member`, y `Library`.

```py
# biblioteca.py:7
class Genre:
```

```py
# biblioteca.py:22
class Book:
```

```py
# biblioteca.py:60
class DigitalBook(Book):
```

```py
# biblioteca.py:87
class Member:
```

```py
# biblioteca.py:115
class Library:
```

### 3. Entornos

#### 3.1. Global

En sí, no hay variables globales, pero sí hay definiciones de clases, funciones, y la importación de los módulos `json` y `memory_management` en el entorno global.

```py
# biblioteca.py:3-4
import json
from memory_management import memory_management
```

### 3.2. Locales

Algunas variables locales son: `member_id`, `name`, `member`, etc.

```py
# biblioteca.py:287-289
member_id = int(input("Ingresa el ID del miembro: "))
name = input("Ingresa el nombre del miembro: ")
member = Member(member_id, name)
```

### 3.3. No locales

No existen variables no locales en la práctica, definidas con la palabra clave `nonlocal`.

### 4. Bloques

Las definiciones de las clases y funciones son bloques, así como los bloques de código dentro de las funciones. Un bloque en Python son definidos por la indentación.

```py
# biblioteca.py:7-19
class Genre: # Bloque 1 (Inicio)
    '''Clase para definir los generos de los libros'''
    FICTION = "Ficcion"
    NON_FICTION = "No Ficcion"
    SCIENCE = "Ciencia"
    HISTORY = "Historia"
    FANTASY = "Fantasia"
    BIOGRAPHY = "Biografia"
    OTHER = "Otro"

    @classmethod
    def all_genres(cls): # Bloque 2 (Inicio)
        return [cls.FICTION, cls.NON_FICTION, cls.SCIENCE, cls.HISTORY, cls.FANTASY, cls.BIOGRAPHY, cls.OTHER]
    # Bloque 2 (Fin)
# Bloque 1 (Fin)
```

### 5. Alcance

#### 5.1. Bloques en línea anidados

```py
# biblioteca.py:115,139-149
class Library: # Bloque 1 (Inicio)
    # ...
    def display_books(self): # Bloque 2 (Inicio)
        '''Método para mostrar los libros disponibles en la biblioteca'''
        if not self.books: # Bloque 3 (Inicio)
            print("\nNo hay libros disponibles.\n")
            return
        # Bloque 3 (Fin)
        print("\nLibros disponibles en biblioteca:\n")
        for book in self.books: # Bloque 4 (Inicio)
            print(f"ID libro: {book.id}\nTitulo: {book.title}\nAutor: {book.author}\nAno de publicacion: {book.publication_year}\nGenero: {book.genre}\nCantidad: {book.quantity}\n")
            if isinstance(book, DigitalBook): # Bloque 5 (Inicio)
                print(f"Formato de archivo: {book.file_format}\n")
            # Bloque 5 (Fin)
        # Bloque 4 (Fin)
        memory_management.display_memory_usage()
    # Bloque 2 (Fin)
    # ...
# Bloque 1 (Fin)
```

#### 5.2. Alcance en funciones

Las siguientes variable en `main()` son locales a la función:

```py
# biblioteca.py:252,258,270-277
def main():
    # ...
    while True:
        # ...
        if choice == 1:
            book_id = int(input("Ingresa ID del libro: "))
            title = input("Ingresa titulo del libro: ")
            author = input("Ingresa nombre del autor: ")
            publication_year = int(input("Ingresa el ano de publicacion: "))
            genre = input("Ingresa el genero del libro: ")
            quantity = int(input("Ingresa la cantidad de libros: "))
            is_digital = input("Es un libro digital? (s/n): ").lower() == 's'
            # ...
        # ...
    # ...
```

### 6. Administración de memoria

#### 6.1. Almacenamiento estático

Existen algunos métodos que son estáticos, llamados `from_dict`:

```py
# biblioteca.py:47-57
@staticmethod
def from_dict(data):
    '''Método para crear un objeto libro a partir de un diccionario'''
    return Book(
        data["id"],
        data["title"],
        data["author"],
        data["publication_year"],
        data["genre"],
        data["quantity"]
    )
```

Pero en sí, no existen variables estáticas en Python de la misma forma que en C.

#### 6.2. Almacenamiento automático

Aunque en Python no existe el concepto de almacenamiento automático como en C, las variables locales dentro de las funciones son creadas y destruidas automáticamente al entrar y salir de la función, lo cual es similar.

```py
# biblioteca.py:271-277
book_id = int(input("Ingresa ID del libro: "))
title = input("Ingresa titulo del libro: ")
author = input("Ingresa nombre del autor: ")
publication_year = int(input("Ingresa el ano de publicacion: "))
genre = input("Ingresa el genero del libro: ")
quantity = int(input("Ingresa la cantidad de libros: "))
is_digital = input("Es un libro digital? (s/n): ").lower() == 's'
```

#### 6.3. Almacenamiento de hilo local o subproceso

El código no tiene almacenamiento de hilo local o subproceso, ya que no se utilizan hilos o subprocesos en la práctica.

#### 6.4. Almacenamiento dinámico

La mayoría de los objetos en Python son creados dinámicamente, como las instancias de las clases `Book`, `DigitalBook`, `Member`, y `Library`.

```py
# biblioteca.py:254
library = Library()
```

### 7. Expresiones

```py
# biblioteca.py:135
if book.id == book_id:
```

```py
# biblioteca.py:174
book.quantity += 1
```

### 8. Comandos

En Python, los comandos son las instrucciones que se ejecutan.

```py
# biblioteca.py:287
member_id = int(input("Ingresa el ID del miembro: "))
```

### 9. Secuencia

#### 9.1. Selección

```py
# biblioteca.py:270,284,309
if choice == 1:
    # ...
elif choice == 2:
    # ...
# ...
else:
    # ...
```

#### 9.2. Iteración

```py
# biblioteca.py:134-136
for book in self.books:
    if book.id == book_id:
        return book
```

```py
# biblioteca.py:258
while True:
```

#### 9.3. Recursión

El programa no tiene recursión.

#### 9.4. Subprogramas

El subprograma `main()` es el punto de entrada del programa.

```py
# biblioteca.py:252
def main():
    # ...
    
```

Los métodos de las clases también son subprogramas.

```py
# biblioteca.py:115,126-130
class Library:
    # ...
    def add_book(self, book):
        '''Método para agregar un libro a la biblioteca'''
        self.books.append(book)
        print("\nEl libro fue agregado exitosamente!\n")
        memory_management.display_memory_usage()
    # ...
```

### 10. Tipos de datos

Los tipos de datos nativos utilizados son: `int`, `str`, `bool`, `list`, y `None`.

Las clases `Book`, `DigitalBook`, `Member`, y `Library` son tipos de datos definidos por el usuario.

[Regresar al inicio](#tabla-de-contenido)
