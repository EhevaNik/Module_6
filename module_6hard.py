from math import pi, sqrt

class Figure:
    sides_count = 0
    def __init__(self, sides, color):
        self.__sides = sides  # список сторон (целые числа)
        self.__color = color # список цветов в формате RGB
        self.filled = False # закрашенный, bool
# Метод get_color, возвращает список RGB цветов.
    def get_color(self):
        return list(self.__color)
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
# перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне
# от 0 до 255 (включительно).
    def __is_valid_color(self, r, g,b):
       if 0 < r < 255 and 0 < g < 255 and 0 < b < 255: # корректный цвет
           return r, g, b
       else:
           self.__color # некорректный цвет

# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        
# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если
# все стороны целые положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides(self, *new_sides):
        for i in new_sides:
            if i > 0:
                if len(new_sides) == self.sides_count:
                    return True
                else:
                    return False
# Метод get_sides должен возвращать значение атрибута __sides.
    def get_sides(self):
        return self.__sides
# Метод __len__ должен возвращать периметр фигуры.
    def __len__(self):
        return sum(self.__sides)
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
# то не изменять, в противном случае - менять
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):  # (Цвет, стороны)
        if len(sides) != 1:
            sides = [1]

        super().__init__(color, sides)
        # радиус рассчитан по формуле R = C / 2π исходя из длины окружности (одной единственной стороны)
        self.__radius = self.get_sides()[0] / (2 * pi)
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
# Площадь круга равна πr², где r — радиус круга.
    def get_square(self):
        return pi * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона).
# Фо́рмула Герона — формула для вычисления площади треугольника S по длинам его сторон a,b,c
# квадратный корень из p*(p-a)*(p-b)*(p-c)
    def get_square(self):
        p = 0.5 * len(self)
        return sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__([sides] * 12, color)
        self.__sides = sides
# Метод get_volume, возвращает объём куба. Объём куба определяется по формуле: V = a³, где a — сторона куба
    def get_volume(self):
        return self.get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
