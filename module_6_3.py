class Horse:
    def __init__(self):
        self.x_distance = 0 # пройденный путь
        self.sound = 'Frrr' # звук, который издаёт лошадь
        super().__init__()

    # Метод где dx - изменение дистанции, увеличивает x_distance на dx
    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
       self.y_distance = 0 # высота полёта
       self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл

    # Метод, где dy - изменение дистанции, увеличивает y_distance на dy
    def fly(self, dy):
       self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)


    # Метод, где dx и dy изменения дистанции. В этом методе должны запускаться
    # наследованные методы run и fly соответственно.
    def move(self, dx, dy):
        Horse.run(self,dx)
        Eagle.fly(self,dy)

    # Метод возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    # Метод, который печатает значение унаследованного атрибута sound.
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
