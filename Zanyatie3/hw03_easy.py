__author__ = 'Вершинин Иван Александрович'

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]
for i, v in enumerate(fruits):
    print('{}.{:>7}'.format(i+1, v))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

a = ["яблоко", "банан", "киви", "арбуз"]
b = ["банан","арбуз","кокос"]

for i in b:
    try:
        a.remove(i)
    except ValueError:
        pass
print(a) 

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

k = range(20)
l = []

for i in k:
    if i%2 == 0:
        l.append(i/4)
    else:
        l.append(i*2)
print(l)