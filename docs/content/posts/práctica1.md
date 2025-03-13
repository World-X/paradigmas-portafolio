+++
date = '2025-03-13T10:02:42-07:00'
draft = true
title = 'Práctica 1'
+++

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

#### 3.1. Variables

```c
// biblioteca.c:7
static int static_var = 0;
```

### 4. Bloques

Esta porción de código muestra dos bloques de código, uno para la función `genreToString` y otro para el `switch` dentro de la misma.

```c
// biblioteca.c:59-70
const char* genreToString(genre_t genre) {
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
}
```

### 5. Alcance

#### 5.1. Global

```c
// memory_management.h:12-15
extern int heap_allocations; // heap_allocations
extern int heap_deallocations; // heap_deallocations
extern int stack_allocations; // stack_allocations
extern int stack_deallocations; // stack_deallocations
```

#### 5.2. Archivo

```c
// biblioteca.c:7
static int static_var = 0;
```

#### 5.3. Local

```c
// biblioteca.c:98.addBook<void>(book_t **, int *)
int genre;
```

```c
// biblioteca.c:170.issueBook<void>(book_t **, member_t *)
int bookID, memberID;
```

```c
// biblioteca.c:212.returnBook<void>(book_t *, member_t *)
int bookID, memberID;
```

### 6. Administración de memoria



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



### 9. Secuencia



### 10. Selección



### 11. Iteración

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

### 12. Recursión

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

### 13. Subprogramas



### 14. Tipos de datos

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
