# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task import SmartBulb, Wardrobe, Triangle

if __name__ == "__main__":
 # TODO: инстанцировать все описанные классы, создав три объекта.C()
    S = SmartBulb(50, 'white', False)
    W = Wardrobe(shelves = 15)
    T = Triangle(5, 3, 30)

    try:
     # TODO: вызвать метод с некорректными аргументами(b)
        S.set_color('rgrg')
    except ValueError:
        print('Ошибка: неправильные данные 1')


    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        W.add_shelf(-2)
    except ValueError:
        print('Ошибка: неправильные данные 2')








    try:
     # TODO: вызвать метод с некорректными аргументами(a)
        T.get_area(-2)
    except ValueError:
        print('Ошибка: неправильные данные 3')
