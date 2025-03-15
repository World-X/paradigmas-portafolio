+++
date = '2025-03-13T10:02:42-07:00'
draft = false
title = 'Práctica 1'
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

Algunos nombres (identificadores) son: `static_var`, `bss_var`, `FICTION`, `NON_FICTION`, `SCIENCE`, `HISTORY`, `FANTASY`, `BIOGRAPHY`, `OTHER`, `genre_t`, `new_book`.

```c
// biblioteca.c:7
static int static_var = 0; // static_var
```

```c
// biblioteca.c:10
int bss_var; // bss_var
```

```c
// biblioteca.c:12-20
typedef enum { // FICTION, NON_FICTION, SCIENCE, HISTORY, FANTASY, BIOGRAPHY, OTHER, genre_t
    FICTION,
    NON_FICTION,
    SCIENCE,
    HISTORY,
    FANTASY,
    BIOGRAPHY,
    OTHER
} genre_t;
```

```c
// biblioteca.c:74
book_t *new_book = (book_t *) malloc(sizeof(book_t)); // new_book
```

### 2. Objetos

No hay clases u objetos en C, y a pesar que lo más cercano son las estructuras, todas son creadas de forma dinámica.

### 3. Entornos

#### 3.1. Global

```c
// memory_management.h:12-15
extern int heap_allocations;
extern int heap_deallocations;
extern int stack_allocations;
extern int stack_deallocations;
```

### 3.2. Locales

```c
// biblioteca.c:170
int bookID, memberID;
```

### 3.3. No locales

No existen variables no locales en C.

### 4. Bloques

Esta porción de código muestra dos bloques de código, uno para la función `genreToString` y otro para el `switch` dentro de la misma.

```c
// biblioteca.c:59-70
const char* genreToString(genre_t genre) { // Bloque 1 (inicio)
    switch (genre) { // Bloque 2 (inicio)
        case FICTION: return "Ficcion";
        case NON_FICTION: return "No Ficcion";
        case SCIENCE: return "Ciencia";
        case HISTORY: return "Historia";
        case FANTASY: return "Fantasia";
        case BIOGRAPHY: return "Biografia";
        case OTHER: return "Otro";
        default: return "Desconocido";
    } // Bloque 2 (fin)
} // Bloque 1 (fin)
```

### 5. Alcance

#### 5.1. Bloques en línea anidados

```c
// biblioteca.c:113-122
book_t* findBookById(book_t *library, int bookID) { // Bloque 1 (inicio)
    book_t *current = library;
    while (current) { // Bloque 2 (inicio)
        if (current->id == bookID) { // Bloque 3 (inicio)
            return current;
        } // Bloque 3 (fin)
        current = current->next;
    } // Bloque 2 (fin)
    return NULL;
} // Bloque 1 (fin)
```

#### 5.2. Alcance en funciones

`bookFound` y `memberFound` son variables locales en las funciones `issueBook` y `returnBook`, es decir, su alcance es solo dentro de las funciones, no son las mismas variables.

```c
// biblioteca.c:169-177,209
void issueBook(book_t *library, member_t *members) {
    int bookID, memberID;
    printf("\nIngresa el ID del miembro: ");
    scanf("%d", &memberID);
    printf("Ingresa el ID del libro: ");
    scanf("%d", &bookID);

    book_t *bookFound = NULL;
    member_t *memberFound = NULL;
    // ...
}
```

```c
// biblioteca.c:211-219,264
void returnBook(book_t *library, member_t *members) {
    int bookID, memberID;
    printf("\nIngresa el ID del miembro: ");
    scanf("%d", &memberID);
    printf("Ingresa el ID del libro: ");
    scanf("%d", &bookID);

    book_t *bookFound = NULL;
    member_t *memberFound = NULL;
}
```

### 6. Administración de memoria

#### 6.1. Almacenamiento estático

```c
// biblioteca.c:7
static int static_var = 0;
```

#### 6.2. Almacenamiento automático

```c
// biblioteca.c:170
int bookID, memberID;
```

#### 6.3. Almacenamiento de hilo local o subproceso

No hay almacenamiento de hilo local o subproceso en C.

#### 6.4. Almacenamiento dinámico

```c
// biblioteca.c:74
book_t *new_book = (book_t *) malloc(sizeof(book_t));
```

### 7. Expresiones

```c
// biblioteca.c:116-118
if (current->id == bookID) { // current->id == bookID
    return current;
}
```

```c
// biblioteca.c:181-184
if (current_book->id == bookID && current_book->quantity > 0) { // current_book->id == bookID && current_book->quantity > 0
    bookFound = current_book;
    break;
}
```

```c
// biblioteca.c:198
bookFound->quantity--; // bookFound->quantity--
```

### 8. Comandos

No hay comandos en C.

### 9. Secuencia

#### 9.1. Selección

```c
// biblioteca.c:75-78
if (!new_book) {
    printf("Error al asignar memoria para el nuevo libro.\n");
    return;
}
```

```c
// biblioteca.c:60-69
switch (genre) {
    case FICTION: return "Ficcion";
    case NON_FICTION: return "No Ficcion";
    case SCIENCE: return "Ciencia";
    case HISTORY: return "Historia";
    case FANTASY: return "Fantasia";
    case BIOGRAPHY: return "Biografia";
    case OTHER: return "Otro";
    default: return "Desconocido";
}
```

#### 9.2. Iteración

```c
// biblioteca.c:362-364
for (int i = 0; i < current->issued_count; i++) { // i
    fprintf(file, "%d\n", current->issued_books[i]);
}
```

```c
// biblioteca.c:392-394
for (int i = 0; i < new_member->issued_count; i++) { // i
    fscanf(file, "%d\n", &new_member->issued_books[i]);
}
```

#### 9.3. Recursión

```c
// biblioteca.c:124-131.displayBooksRecursive<void>(book_t *)
void displayBooksRecursive(book_t *library) {
    if (!library) {
        return;
    }
    printf("\nID libro: %d\nTitulo: %s\nAutor: %s\nAno de publicacion: %d\nGenero: %s\nCantidad: %d\n",
        library->id, library->title, library->author, library->publication_year, genreToString(library->genre), library->quantity);
    displayBooksRecursive(library->next);
}
```

#### 9.4. Subprogramas

No hay subprogramas en C.

### 10. Tipos de datos

```c
// biblioteca.c:12-20
typedef enum { // genre_t
    FICTION,
    NON_FICTION,
    SCIENCE,
    HISTORY,
    FANTASY,
    BIOGRAPHY,
    OTHER
} genre_t;
```

```c
// biblioteca.c:22-30
typedef struct _book { // book_t
    int id;
    char title[100];
    char author[100];
    int publication_year;
    genre_t genre;
    int quantity;
    struct _book *next;
} book_t;
```

```c
// biblioteca.c:32-38
typedef struct _member { // member_t
    int id;
    char name[100];
    int issued_count;
    int *issued_books;
    struct _member *next;
} member_t;
```

```c
// memory_management.c:10-14
typedef struct MemoryRecord { // MemoryRecord
    void *pointer;
    size_t size;
    struct MemoryRecord *next;
} MemoryRecord;
```

[Regresar al inicio](#tabla-de-contenido)
