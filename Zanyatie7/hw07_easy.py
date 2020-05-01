import math
__author__ = 'Вершинин Иван Александрович'
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle(object):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        try:
            self.x1 = int(x1)
            self.y1 = int(y1)
            self.x2 = int(x2)
            self.y2 = int(y2)
            self.x3 = int(x3)
            self.y3 = int(y3)
        except ValueError:
            print("Неправельно введены данные")

        self.ab = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.ac = math.sqrt((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2)
        self.bc = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)   

    def square(self):
        return  0.5 * abs((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3)) 
    def height(self):
        height = 2 * self.square() / self.ac
        return f'Высота треугольника = {height}'
    def perimeter(self):
        perimeter = self.ab + self.ac + self.bc
        return f'Периметр треугольника = {perimeter}'


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapezoid(object):
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        try:
            self.x1 = int(x1)
            self.y1 = int(y1)
            self.x2 = int(x2)
            self.y2 = int(y2)
            self.x3 = int(x3)
            self.y3 = int(y3)
            self.x4 = int(x4)
            self.y4 = int(y4)
        except ValueError:
            print("Неправельно введены данные")
        self.ab = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        self.bc = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        self.cd = math.sqrt((self.x4 - self.x3) ** 2 + (self.y4 - self.y3) ** 2)
        self.ad = math.sqrt((self.x4 - self.x1) ** 2 + (self.y4 - self.y1) ** 2)
            
        if self.bc < self.ad:
            self.s_base = self.bc
            self.l_base = self.ad
        else:
            self.small_base = self.ad
            self.larger_base = self.bc

    def _heigh(self):
        a = self.s_base
        b = self.l_base
        c = self.ab ** 2
        d = self.cd ** 2
        h = math.sqrt(c - 1/4 * ((c - d) / (b - a) + b - a) ** 2)
        return h

    def square(self):
        square = ((self.s_base + self.l_base) / 2) * self._heigh()
        return f'Площадь трапеции = {square}'

    def perimeter(self):
        perimeter = self.ab + self.bc + self.cd + self.ad
        return f'Периметр трапеции = {perimeter}'
    def equal_part(self):
        if self.ab == self.cd:
            return "Равнобочная трапеция"
        else:
            return "Не равнобочная трапеция"
    def lines(self):
        return f'Длины сторон трапеции:\n AB = {self.ab} \n BC = {self.bc} \n CD = {self.cd} \n AD = {self.ad}'


if __name__ == '__main__':

    triangle1 = Triangle(1, 4, 3, 4, 5, 6)
    triangle2 = Triangle(-1, -2, -3, -2, -6, -3)
    triangle3 = Triangle(0, 0, 7, 4, -3, 2)

    print(triangle1.square())
    print(triangle2.perimeter())
    print(triangle3.height())

    trapezium1 = Trapezoid(1, 1, 5, 7, 8, 7, 10, 1)
    trapezium2 = Trapezoid(1, 1, 3, 7, 8, 7, 10, 1)

    print(trapezium1.perimeter())
    print(trapezium1.lines())
    print(trapezium2.lines())
    print(trapezium2.equal_part())



