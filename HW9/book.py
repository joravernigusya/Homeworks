class Genre:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description


class Book(Genre):
    def __init__(self, name, description, title, author):
        super().__init__(name, description)
        self._title = title
        self._author = author

    def __str__(self):
        return f"{self._title}, автор: {self._author}, жанр: {self.get_name()}"

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author


genre1 = Genre(
    "Научная фантастика",
    "Художественная литература, основанная на научных разработках/открытиях",
)
book1 = Book(
    "Научная фантастика",
    "Художественная литература, основанная на научных разработках/открытиях",
    "Война миров",
    "Герберт Уэллс",
)

genre2 = Genre("Фэнтези", "Художественная литература с воображаемыми элементами")
book2 = Book(
    genre2.get_name(),
    genre2.get_description(),
    "Властелин колец",
    "Дж. Р. Р. Толкин",
)

print(book1)
print(book2)
