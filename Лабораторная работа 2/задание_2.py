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

# TODO: написать класс Library
class Library:

    def __init__(self, books=0):
        if not books:
            self.books = []
        else:
            self.books = books

    def get_next_book_id(self):

        if self.books == []:
            return 1

        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_:int):
        if not isinstance(id_, int):
            raise TypeError(f"{id_=} должно быть целым числом")

        for i, b in enumerate(self.books):
            
            
            if b.id == id_:
                return i

        raise ValueError(f"Книги с индентификатором {id_} нет в библиотеке")



if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

