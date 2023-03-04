class Book:
    """Добавление и удаление книг из библиотеки,
    а также поиск книг по атрибутам.
    """

    def __init__(self, title, author, genre):
        self._title = title
        self._author = author
        self._genre = genre

    def __str__(self):
        return (
            f"Название: {self._title}, Aвтор: {self._author}, " f"Жанр: "
            f"{self._genre}"
        )

    def add_to_library(self, library):
        library.append(self)

    def remove_from_library(self, library):
        if self in library:
            library.remove(self)

    @staticmethod
    def find_by_title(title, library):
        return [book for book in library if book._title == title]

    @staticmethod
    def find_by_author(author, library):
        return [book for book in library if book._author == author]

    @staticmethod
    def find_by_genre(genre, library):
        return [book for book in library if book._genre == genre]

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_genre(self):
        return self._genre


class Fiction(Book):
    def __init__(self, title, author):
        super().__init__(title, author, "Художественный")


class NotFiction(Book):
    def __init__(self, title, author):
        super().__init__(title, author, "Не художественный")


# Создаем объекты книги.
book1 = Fiction("1984", "George Orwell")
book2 = Fiction("Shantaram", "Gregory David Roberts")
book3 = NotFiction("Flowers for Algernon", "Daniel Keyes")

# Создаем пустой список для библиотеки.
library = []

# Добавляем книги в библиотеку.
book1.add_to_library(library)
book2.add_to_library(library)
book3.add_to_library(library)

# Поиск книги по его названию.
book_found_by_title = Book.find_by_title("1984", library)
for book in book_found_by_title:
    print(book)

# Вывод количетсва художетсвенных книг.
fiction_book = [book for book in library if isinstance(book, Fiction)]
print(f"Количество художественных книг в библиотеке: {len(fiction_book)}")

# Вывод количетсва не художетсвенных книг.
not_fiction_book = [book for book in library if isinstance(book, NotFiction)]
print(f"Количество не художественных книг в библиотеке:" 
      f" {len(not_fiction_book)}")
