# TODO: Подробно описать три произвольных класса

import math
# TODO: описать класс


class SmartBulb:

    """
    Этот класс описывает умную лампу
    """

    def __init__(self, brightness: int = 50, color: str = "white", is_on: bool = False):
        """
        Инициализация умной лампочки.

        param brightness: Яркость (0-100%, по умолчанию 50)
        param color: Цвет (из разрешенного списка)
        param is_on: Включена ли лампа (по умолчанию False)
        """
        self.brightness = brightness
        self.color = color
        self.is_on = is_on

    def change_brightness(self, level: int = 50) -> None:
        """
        Изменяет яркость лампы.

        param level: Новый уровень яркости (0-100)
        raises ValueError: Если уровень вне диапазона
        """
        if not 0 <= level <= 100:
            raise ValueError("Яркость должна быть от 0 до 100%")
        self.brightness = level

    def set_color(self, color: str) -> None:
        """
        Устанавливает цвет лампы.

        :param color: Новый цвет (из списка разрешенных)
        :raises ValueError: Если цвет не поддерживается
        """
        allowed_colors = ["white", "red", "blue", "green", "yellow"]
        if color.lower() not in allowed_colors:
            raise ValueError(f"Цвет должен быть одним из: {allowed_colors}")
        self.color = color.lower()

    def toggle_power(self) -> bool:
        """
        Переключает состояние лампы (вкл/выкл).

        return: Текущий статус (is_on)
        """
        self.is_on = not self.is_on
        return self.is_on

# TODO: описать ещё класс


class Wardrobe:

    '''
    Класс описывает какой-либо шкаф
    '''

    def __init__(self, shelves: int, materail='сосна'):  #Создание шкафа
        #shelves - количество полок
        # material - материал шкафа
        Wardrobe.varify_data_int(shelves)
        Wardrobe.varify_data_str(materail)

        self.shelves = shelves
        self.material = materail

        self.items = []  #список предметов в шкафу(Изначально шкаф пустой)

    @staticmethod
    def varify_data_int(x):
        if not isinstance(x, int) or x < 0:
            raise ValueError('Переменая должна быть целым положительным числом')

    @staticmethod
    def varify_data_str(x):
        if not isinstance(x, str):
            raise ValueError('Переменная должна быть типа str')

    def add_shelf(self, x=1):  #добавление полок

        Wardrobe.varify_data_int(x)
        self.shelves += x

    def add_item(self, item: str):  #положить что-то в шкаф
        Wardrobe.varify_data_str(item)
        self.item.append(item)

    def take(self, item):  # взять предмет из шкафа
        Wardrobe.varify_data_str(item)
        if item in self.items:
            self.items.remove(item)
            return item
        else:
            return f'Предмета {item} нет в шкафу'

# TODO: и ещё один
class Triangle:

    '''
    This class describes any Triangle
    '''

    def __init__(self, side_a: tuple[int, float], side_b: tuple[int, float], angle: tuple[int, float]):

        #  side_a - длина одной стороны
        #  side_b - длина другой стороны
        #  angle - угол между этими сторонами в градусах

        #  проверка допустимости значений переменных
        Triangle.varify_data(side_a)
        Triangle.varify_data(side_b)
        Triangle.varify_data(angle)

        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle
        self.side_c = self.calculate_third_side()

    @staticmethod
    def varify_data(x):

        '''
        Метод для проверки данных, которые должны быть положительными числами
        '''

        if not isinstance(x, (int, float)) or x < 0:
            raise ValueError(f'Переменная {x=} должна быть положительным числом')



    def calculate_third_side(self) -> float:

        #  считает стретью сторону треугольника

        #  перевод из градусов в радианы
        angle_rad = math.radians(self.angle)
        return math.sqrt(self.side_a ** 2 + self.side_b ** 2 - 2 * self.side_a * self.side_b * math.cos(angle_rad))

    def get_area(self, precision=2) -> float:

        '''
        Вычисляет площадь треугольника
        '''

        #  precision - количество знаков после запятой

        Triangle.varify_data(precision)

        area = 0.5 * self.side_a * self.side_b * math.sin(math.radians(self.angle))

        return round(area, precision)

    def get_perimetr(self) -> float:

        #  этот метод считает периметр
         return self.side_a + self.side_b + self.side_c




