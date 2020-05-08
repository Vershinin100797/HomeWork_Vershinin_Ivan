import random

__author__ = 'Вершинин Иван Александрович'
#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""


class Playing_Card(object):
    def __init__(self, name, computer=0):
        self.name = name
        self.computer = computer
        self.creating_card()

    def creating_card(self):
        self.card = [[' ' for i in range(0, 9)],
                          [' ' for i in range(0, 9)],
                          [' ' for i in range(0, 9)]]  
        rand_nums = sorted(list(random.sample(range(1, 91), 15)))

        k = 0
        for ln in range(3):
            idx = sorted(list(random.sample(range(0, 9), 5)))
            for i in range(5):
                self.card[ln][idx[i]] = rand_nums[k]
                k += 1

        return self.card

    def open_card(self):

        if self.computer == 0:
            self.nm = 'Игрок'
        else:
            self.nm = 'Компьютер'

        l2 = 17 - len(self.name) // 2
        l1 = l2
        if len(self.name) % 2 != 0:
            l1 = l2 - 1

        l4 = 17 - len(self.nm) // 2
        l3 = l4
        if len(self.nm) % 2 != 0:
            l3 = l4 - 1

        print('-' * l1 + ' ' + self.name + ' ' + '-' * l2)

        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                print('{:3}'.format(self.card[i][j]), end=' ')
            print()

        print('-' * l3 + ' ' + self.nm + ' ' + '-' * l4 + '\n')


class Barrels(object):
    def __init__(self):
        self.set_barrels()

    def set_barrels(self):
        self.barrel_list = [i for i in range(1, 91)]
        return self.barrel_list

    def show_barrel(self):
        self.number = random.choice(self.barrel_list)
        self.barrel_list.remove(self.number)
        return self.number


class Game(object):
    def __init__(self, player=str, opponent=str):
        self.player = player
        self.opponent = opponent
        self.run_game(player, opponent)


    def check_win(self, z):
        x = 0
        for i in range(len(z.card)):
            for j in range(len(z.card[i])):
                if type(z.card[i][j]) is int:
                    x += int((z.card[i][j]))
        if x == 0:
            print(f'Игрок {z.name} победил!')
            return False

    def check(self, x, y):
        if x.computer == 0:
            result = 'X'
            print(f'Ход игрока: {x.name}')
            while result != 'Y' and result != 'N' and result != 'y' and result != 'n':
                result = input('Зачеркнуть цифру? (Y/N)')
                if result != 'Y' and result != 'N' and result != 'y' and result != 'n':
                    print('Не верное значение. Введите Y или N!')

            flag = 0
            if result == 'Y' or result == 'y':
                for line in range(len(x.card)):
                    if y.number in x.card[line]:
                        id = int(x.card[line].index(y.number))
                        x.card[line][id] = '_'
                        flag = 1
                if flag != 1:
                    print(f'Игрок {x.name} проиграл!')
                    return False

            elif result == 'N' or result == 'n':
                for line in range(len(x.card)):
                    if y.number in x.card[line]:
                        print(f'Игрок {x.name} проиграл!')
                        return False

        else:
            for line in range(len(x.card)):
                if y.number in x.card[line]:
                    id = int(x.card[line].index(y.number))
                    x.card[line][id] = '_'

    def run_game(self, player, opponent):

        barrel_bag = Barrels()

        print('Первый игрок: ')
        self.pl_name = input('Введите имя первого игрока: ')
        self.pl_is_comp = int(input(f'{self.pl_name} - человек или компьютер? 0 - человек, 1 - компьютер: '))

        print('Второй игрок: ')
        self.op_name = input('Введите имя второго игрока: ')
        self.op_is_comp = int(input(f'{self.op_name} - человек или компьютер? 0 - человек, 1 - компьютер: '))

        player = Playing_Card(self.pl_name, computer=self.pl_is_comp)
        opponent = Playing_Card(self.op_name, computer=self.op_is_comp)

        print('\nИгра начинаеться.\n')

        while True:

            barrel_bag.show_barrel()
            print(f'\nСледующий бочонок: {barrel_bag.number} (осталось {len(barrel_bag.barrel_list)}) \n')

            player.open_card()
            opponent.open_card()

            if self.check(player, barrel_bag) is False or self.check(opponent, barrel_bag) is False or self.check_win(
                    player) is False or self.check_win(opponent) is False:
                return False

            print('')


if __name__ == '__main__':
    start_game = Game()
