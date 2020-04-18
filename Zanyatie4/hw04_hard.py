import re
__author__ = 'Вершинин Иван Александрович'

# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

def diff(lst):
    difference = lst[0]
    for x in range(len(lst)):
        if x:
            difference = difference - lst[x]
    return difference

def search_nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def search_nok(a, b):
    return a * b / search_nod(a, b)
    
def format_dec(num, NOK):
    if num > NOK:
        cel = num // NOK
        new_num = num % NOK
        result = '{0:.0f} {1:.0f}/{2:.0f}'.format(cel, new_num, NOK)
    else:
        result = '{0:.0f}/{1:.0f}'.format(num, NOK)
    return result

equation = input('Введите дроби: ')
params = re.findall(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
funcs = re.split(r'[-]?[0-9]+/[0-9]+|[-]?[0-9]+', equation)
nums = []
noms = []
i = 0
for param in params:
    temp = param.split('/')
    nums.append(int(temp[0]))
    if len(temp) > 1:
        noms.append(int(temp[1]))
    else:
        noms.append(1)
for p in funcs:
    if p:
        func = p.strip()
        break
NOK = search_nok(noms[0], noms[1])
for n in nums:
    nums[i] = n * NOK / noms[i]
    i += 1
print(f'Результат вычисления {equation} : ')
if func == '+':
    print(format_dec(sum(nums), NOK))
elif func == '-':
    print(format_dec(diff(nums), NOK))
else:
    print('Действие не определено')

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def payroll(x):
    mani,clock,real_clock = list(map(int,x))
    if clock > real_clock:
        res = mani/clock*real_clock
    else:
        res = mani + (mani/clock * real_clock - clock)*2
    return int(res)

with open('data/workers',encoding='utf-8') as inp, open('data/hours_of',encoding='utf-8') as clock:
    list_norm = inp.read().split('\n')
    list_real = clock.read().split('\n')

def workers_data(x):
    x = x.split()
    name,mani,clock = ' '.join(x[:2]),x[2],x[4]
    return name,[mani,clock]

full_data = dict()
for x in list_norm[1:]:
    name,data = workers_data(x)
    full_data[name] = data
for i in list_real[1:]:
    i = i.split()
    full_data[' '.join(i[:2])].append(i[-1])

with open('data/payroll.txt', 'w', encoding='utf-8') as out:
    out.write('Имя Фамилия  Зарплата  Норма_часов  Отработано  К выдаче\n')
    for name in full_data:
        out.write('{:>2}  {:>2}  {:>2}  {:>2}   {:>2}\n'.format(name,*(full_data[name]),payroll(full_data[name])))

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

dikt_fruts = dict()
with open('data/fruits.txt',encoding='utf-8') as inp_ut:
    for fruits in inp_ut.readlines():
        if fruits == "\n":
            continue
        else:
            file_name = 'fruits_{}'.format(fruits[0].upper())
            dikt_fruts[file_name] = dikt_fruts.get(file_name,'')+fruits
    
for i in dikt_fruts:
    name = 'data/{}.txt'.format(i)
    with open(name,'w',encoding='utf-8') as out:
        out.write(dikt_fruts[i])
print('Формирование файлов по именам фруктов закончено!')