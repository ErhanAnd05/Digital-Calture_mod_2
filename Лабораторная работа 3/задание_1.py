class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    #  Для атрибутов author и name установлены лишь геттеры,
    #  чтобы их нельзя было изменить.
    @property
    def name(self) -> str:
        return self.name

    @property
    def author(self) -> str:
        return self.author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        super().__str__()
        return f"pages={self.pages}"

    @property
    def pages(self) -> int:
        return self.pages

    @pages.setter
    def pages(self, pages_count: int):
        if not isinstance(pages_count, int):
            raise TypeError(f"Неверный тип данных для атрибута {pages_count=}")
        elif pages_count <= 0:
            raise ValueError(f"Атрибут {pages_count=} должен быть целым положительным числом")

        self.pages = pages_count


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        super().__str__()  # Наследовние метода __str__()
        return f"duration={self.duration}"  # Перегрузка

    @property
    def duration(self):

        return self.duration

    @duration.setter  # Ограничение для атрибута duration
    def duration(self, d):
        if not isinstance(d, float):
            raise TypeError(f"Продолжительности книги {d=} должна быть числом с плавающей запятой")

        self.duration = d
