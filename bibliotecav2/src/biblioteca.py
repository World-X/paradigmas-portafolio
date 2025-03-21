from enum import Enum
from dataclasses import dataclass

class Genre(Enum):
    FICTION = 0
    NON_FICTION = 1
    SCIENCE = 2
    HISTORY = 3
    FANTASY = 4
    BIOGRAPHY = 5
    OTHER = 6

@dataclass
class Book:
    _id: int
    title: str
    author: str
    publication_year: int
    genre: Genre
    quantity: int

@dataclass
class Member:
    _id: int
    name: str
    issued_count: int
    issued_books: list[int]

def genre_to_string(genre: Genre) -> str:
    match genre:
        case Genre.FICTION:
            return "Ficcion"
        case Genre.NON_FICTION:
            return "No Ficcion"
        case Genre.SCIENCE:
            return "Ciencia"
        case Genre.HISTORY:
            return "Historia"
        case Genre.FANTASY:
            return "Fantasia"
        case Genre.BIOGRAPHY:
            return "Biografia"
        case Genre.OTHER:
            return "Otro"
        case _:
            return "Desconocido"

def string_to_genre(genre: str) -> Genre:
    match genre:
        case "Ficcion":
            return Genre.FICTION
        case "No Ficcion":
            return Genre.NON_FICTION
        case "Ciencia":
            return Genre.SCIENCE
        case "Historia":
            return Genre.HISTORY
        case "Fantasia":
            return Genre.FANTASY
        case "Biografia":
            return Genre.BIOGRAPHY
        case _:
            return Genre.OTHER

def add_book(library: list[Book]) -> None:
    _id: int = int(input("Ingresa ID del libro: "))
    title: str = input("Ingresa titulo del libro: ")
    author: str = input("Ingresa nombre del autor: ")
    publication_year: int = int(input("Ingresa el año de publicacion: "))
    genre: Genre = Genre(int(input("Ingresa el genero del libro (0: FICTION, 1: NON_FICTION, 2: SCIENCE, 3: HISTORY, 4: FANTASY, 5: BIOGRAPHY, 6: OTHER): ")))
    quantity: int = int(input("Ingresa la cantidad de libros: "))
    book: Book = Book(_id, title, author, publication_year, genre, quantity)
    library.append(book)
    print("El libro fue agregado exitosamente!")

def display_books(library: list[Book]) -> None:
    if len(library) == 0:
        print("No hay libros disponibles.")
        return
    print("Libros disponibles en biblioteca:")
    for book in library:
        print("ID libro:", book._id)
        print("Titulo:", book.title)
        print("Autor:", book.author)
        print("año de publicacion:", book.publication_year)
        print("Genero:", genre_to_string(book.genre))
        print("Cantidad:", book.quantity)

def add_member(members: list[Member]) -> None:
    _id: int = int(input("Ingresa ID del miembro: "))
    name: str = input("Ingresa nombre del miembro: ")
    member: Member = Member(_id, name, 0, [])
    members.append(member)
    print("Miembro agregado exitosamente!")


def issue_book(library: list[Book], members: list[Member]) -> None:
    member_id: int = int(input("Ingresa el ID del miembro: "))
    book_id: int = int(input("Ingresa el ID del libro: "))

    book_found: Book = None
    member_found: Member = None

    for book in library:
        if book._id == book_id and book.quantity > 0:
            book_found = book
            break

    for member in members:
        if member._id == member_id:
            member_found = member
            break

    if book_found and member_found:
        book_found.quantity -= 1
        member_found.issued_count += 1
        member_found.issued_books.append(book_id)
        print("Libro prestado satisfactoriamente!")
    else:
        print("Libro o miembro no encontrados.")

def return_book(library: list[Book], members: list[Member]) -> None:
    member_id: int = int(input("Ingresa el ID del miembro: "))
    book_id: int = int(input("Ingresa el ID del libro: "))

    book_found: Book = None
    member_found: Member = None

    for book in library:
        if book._id == book_id:
            book_found = book
            break
    
    for member in members:
        if member._id == member_id:
            member_found = member
            break
    
    if book_found and member_found:
        found = False
        for issued_book in member_found.issued_books:
            if issued_book == book_id:
                found = True
                member_found.issued_books.remove(book_id)
                member_found.issued_count -= 1
                break
        if found:
            book_found.quantity += 1
            print("Libro devuelto satisfactoriamente!")
        else:
            print("El miembro no tiene este libro prestado.")
    else:
        print("Libro o miembro no encontrados.")

def display_members(members: list[Member], library: list[Book]) -> None:
    if len(members) == 0:
        print("No hay miembros disponibles.")
        return
    print("Miembros disponibles en biblioteca:")
    for member in members:
        print("ID miembro:", member._id)
        print("Nombre:", member.name)
        print("Cantidad de libros prestados:", member.issued_count)
        for book_id in member.issued_books:
            for book in library:
                if book._id == book_id:
                    print("  Libro ID:", book._id)
                    print("  Titulo:", book.title)
                    print("  Autor:", book.author)

def search_member(members: list[Member], library: list[Book]) -> None:
    member_id: int = int(input("Ingresa el ID del miembro: "))

    member_found: Member = None

    for member in members:
        if member._id == member_id:
            member_found = member
            break
    
    if member_found:
        print("ID miembro:", member_found._id)
        print("Nombre:", member_found.name)
        print("Cantidad de libros prestados:", member_found.issued_count)
        for book_id in member_found.issued_books:
            for book in library:
                if book._id == book_id:
                    print("  Libro ID:", book._id)
                    print("  Titulo:", book.title)
                    print("  Autor:", book.author)
    else:
        print("Miembro no encontrado.")

def save_library_to_file(library: list[Book], filename: str) -> None:
    with open(filename, "w") as file:
        for book in library:
            file.write(f"{book._id}\n{book.title}\n{book.author}\n{book.publication_year}\n{genre_to_string(book.genre)}\n{book.quantity}\n")
    print(f"Biblioteca guardada exitosamente en {filename}")

def save_members_to_file(members: list[Member], filename: str) -> None:
    with open(filename, "w") as file:
        for member in members:
            file.write(f"{member._id}\n{member.name}\n{member.issued_count}\n")
            for book_id in member.issued_books:
                file.write(f"{book_id}\n")
    print(f"Miembros guardados exitosamente en {filename}")

def load_library_from_file(library: list[Book], filename: str) -> None:
    try:
        with open(filename, "r") as file:
            for line in file:
                _id = int(file.readline())
                title = file.readline().strip()
                author = file.readline().strip()
                publication_year = int(file.readline())
                genre = string_to_genre(file.readline().strip())
                quantity = int(file.readline())
                book = Book(_id, title, author, publication_year, genre, quantity)
                library.append(book)
        print(f"Biblioteca cargada exitosamente desde {filename}")
    except FileNotFoundError:
        print(f"Error al abrir el archivo para cargar la biblioteca: {filename} no existe")

def load_members_from_file(members: list[Member], filename: str) -> None:
    try:
        with open(filename, "r") as file:
            for line in file:
                _id = int(file.readline())
                name = file.readline().strip()
                issued_count = int(file.readline())
                issued_books = []
                for i in range(issued_count):
                    issued_books.append(int(file.readline()))
                member = Member(_id, name, issued_count, issued_books)
                members.append(member)
        print(f"Miembros cargados exitosamente desde {filename}")
    except FileNotFoundError:
        print(f"Error al abrir el archivo para cargar los miembros: {filename} no existe")

def main():
    library: list[Book] = []
    members: list[Member] = []
    choice: int = 0
    load_library_from_file(library, "library.txt")
    load_members_from_file(members, "members.txt")
    while choice != 8:
        print("Menu de sistema de manejo de biblioteca")
        print("\t1. Agregar un libro")
        print("\t\t- Ingresa los detalles del libro como ID, titulo, autor, año de publicacion, genero y cantidad.")
        print("\t2. Mostrar libros disponibles")
        print("\t\t- Muestra todos los libros disponibles en la biblioteca.")
        print("\t3. Agregar un miembro")
        print("\t\t- Ingresa los detalles del miembro como ID y nombre.")
        print("\t4. Prestar libro")
        print("\t\t- Ingresa el ID del miembro y el ID del libro para prestar el libro al miembro.")
        print("\t5. Devolver libro")
        print("\t\t- Ingresa el ID del miembro y el ID del libro para devolver el libro a la biblioteca.")
        print("\t6. Mostrar miembros disponibles")
        print("\t\t- Muestra todos los miembros disponibles en la biblioteca.")
        print("\t7. Buscar miembro")
        print("\t\t- Busca un miembro por ID y muestra sus detalles.")
        print("\t8. Guardar y salir")
        print("\t\t- Guarda los datos de la biblioteca en un archivo y sale del programa.")
        choice = int(input("Indica tu opcion: "))
        match choice:
            case 1:
                add_book(library)
            case 2:
                display_books(library)
            case 3:
                add_member(members)
            case 4:
                issue_book(library, members)
            case 5:
                return_book(library, members)
            case 6:
                display_members(members, library)
            case 7:
                search_member(members, library)
            case 8:
                save_library_to_file(library, "library.txt")
                save_members_to_file(members, "members.txt")
                print("Saliendo del programa")
            case _:
                print("Esta no es una opcion valida!!!")

if __name__ == "__main__":
    main()
