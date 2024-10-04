class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner #(str)  атрибут владелец транспорта.(владелец может меняться)
        self.__model = __model # (str) # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = __engine_power #(int) # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = __color #(str) # название цвета. (мы не можем менять цвет автомобиля своими руками)

# Метод get_model - возвращает строку: "Модель: <название модели транспорта>"
    def get_model(self):
        return f'Модель: {self.__model}'

# Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

# Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    def get_color(self):
        return f'Цвет: {self.__color}'

# Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
# а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

# Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть
# в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
    def set_color(self, new_color):
        if new_color.lower() in (item.lower() for item in self.__COLOR_VARIANTS):
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')

# Взаимосвязь методов и скрытых атрибутов:
# Методы get_model, get_horsepower, get_color находятся в одном классе с соответствующими им атрибутами:
# __model, __engine_power, __color. Поэтому атрибуты будут доступны для методов.
# Атрибут класса __COLOR_VARIANTS можно получить обращаясь к нему через объект(self).
# Проверка в __COLOR_VARIANTS происходит не учитывая регистр ('BLACK' ~ 'black').

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5 #(в седан может поместиться только 5 пассажиров)

# Исходный код:
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
