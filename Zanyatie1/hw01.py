
__author__ = 'Вершинин Иван Александрович'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...
Name = 'Иван'
Age = 22
print(Name + ' на '+ str(Age - 18) + ' года/лет больше 18')

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
a = input('Введите переменную 1: ')
b = input('Введите переменную 2: ')
a,b = b,a
print('Переменная 1 теперь:',a,'Переменная 2 теперь:',b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
import math

a = float(input('Коэффициент 1: '))
b = float(input('Коэффициент 2: '))
c = float(input('Коэффициент 3: '))

disc = b ** 2 - 4 * a * c

if disc > 0:
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    print('x1 =',x1,'x2 =',x2)
elif disc == 0:
    x = -b / (2 * a)
    print("x =",x)
else:
    print("Корней нет")    
