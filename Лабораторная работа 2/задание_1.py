BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO: написать класс Book

class Book:
    def __init__(self, name: str, id_: int, pages: int):

        """
        Инициализация книги из библиотеки
        """
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Название книги должно быть строкой")

        Book.varifi_data_int(id_)
        Book.varifi_data_int(pages)

        self.id = id_
        self.pages = pages

    @staticmethod
    def varifi_data_int(x):
        """
        Метод для проверки, что x - положительное число
        """

        if not isinstance(x, int):
            raise TypeError(f"Переменная {x=} должна быть типа integer")
        if x <= 0:
            raise ValueError(f"Число {x=} должно быть положительным")

    def __str__(self):

        return f'Книга "{self.name}"'

    def __repr__(self):

        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'


if __name__ == '__main__':

    #  инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
