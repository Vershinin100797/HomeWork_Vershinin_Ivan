from random import choice
__author__ = 'Вершинин Иван Александрович'

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1,fib2 = 0,1
    i = 0
    while True:
        if i>=n:
            print(fib1)
        fib1, fib2 = fib2, fib1 + fib2
        i+=1
        if i>m:
            break

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(nums):
    if len(nums) <= 1:
        return nums
    else:
       rnd_num = choice(nums)
    l_nums = [n for n in nums if n < rnd_num]
    m_nums = [rnd_num] * nums.count(rnd_num)
    r_nums = [n for n in nums if n > rnd_num]
    return sort_to_max(l_nums) + m_nums + sort_to_max(r_nums)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(fnc, any_arg):
    result = []
    for x in any_arg:
        if fnc(x):
            result.append(x)
    return result

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def para(a1, a2, a3, a4):
    if a1[1] == a4[1] and a2[1] == a3[1] and abs(a1[0]-a2[0]) == abs(a3[0]-a4[0]):
        print('это параллелограм') 
    else:
        print('это не параллелограм')


if __name__ == '__main__':
    fibonacci(0, 5)
    
    print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

    line = [1, 2, 3, 4, 5, 6]

    print(my_filter(lambda x : x % 2 == 0, line))

    A1 = (7, 2)
    A2 = (8, 4)
    A3 = (11, 4)
    A4 = (10, 2)

    para(A1, A2, A3, A4)