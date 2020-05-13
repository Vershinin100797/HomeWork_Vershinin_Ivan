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


class PlayerException(Exception):
    def __init__(self, message=None, player=None):
        self.message = message
        self.player = player


class cached_property(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls=None):
        result = instance.__dict__[self.func.__name__] = self.func(instance)
        return result


class Playing_Card(object):
    def __init__(self, name, game_name=None):
        self.name = name or 'Mister X'
        self.game_name = game_name
        self.creating_card()

    def creating_card(self):

        self.card = [['' for i in range(0, 9)],
                          ['' for i in range(0, 9)],
                          ['' for i in range(0, 9)]]
        rand_nums = sorted(random.sample(range(1, 91), 15))

        k = 0
        for ln in range(3):
            idx = sorted(random.sample(range(0, 9), 5))
            for i in range(5):
                self.card[ln][idx[i]] = rand_nums[k]
                k += 1
        return self.card

    def create_line(self, name):
        l2 = 17 - len(name) // 2
        l1 = l2
        if len(name) % 2 != 0:
            l1 = l2 - 1
        return '-' * l1 + ' ' + name + ' ' + '-' * l2

    @cached_property
    def get_header(self):
        return self.create_line(self.name)

    @cached_property
    def get_footer(self):
        return self.create_line(self.game_name)

    def open_card(self):
        print(self.get_header)

        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                print('{:3}'.format(self.card[i][j]), end=' ')
            print()

        print(self.get_footer)

    def get_cart_items(self):
        _temp = []
        for c_item in self.card:
            _new_list = [item for item in c_item if isinstance(item, int)]
            _temp += _new_list
        return _temp

    def del_item(self, item):
        for c_item in self.card:
            if item in c_item:
                c_item[c_item.index(item)] = '-'

    def get_len(self):
        return len(self.get_cart_items())


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
    def __init__(self):
        self.players = []
        self.max_players = 2
        self.barrel_bag = None

    def _check_type(self):
        for player in self.players:
            p_type, p_card = player

            print(f'Ход игрока {p_card.name}')
            if p_type:
                self._check_human(p_card)
            else:
                self._check_robot(p_card)

    def _check_human(self, card):
        while True:
            result = input('Зачеркнуть цифру? (Y/N)')
            if result != 'Y' and result != 'N' and result != 'y' and result != 'n':
                print('Не верное значение. Введите Y или N!')
            elif result == 'Y' or result == 'y':
                result = True
                break
            elif result == 'N' or result == 'n':
                result = False
                break

        if result:
            if self.barrel_bag.number not in card.get_cart_items():
                raise PlayerException(message='Игра окончена, проигравший:', player=card.name)
            else:
                card.del_item(self.barrel_bag.number)
        else:
            if self.barrel_bag.number in card.get_cart_items():
                raise PlayerException(message='Игра окончена, проигравший:', player=card.name)

    def _check_robot(self, card):
        if self.barrel_bag.number in card.get_cart_items():
            card.del_item(self.barrel_bag.number)

    def _check(self):
        try:
            self._check_type()
        except PlayerException as e:
            return e
        return self._check_win()

    def _check_win(self):
        wins = []
        for player in self.players:
            _, card = player
            if card.get_len() == 0:
                wins.append(card)
        return wins or None

    @classmethod
    def run_game(cls):
        self = cls()

        self.barrel_bag = Barrels()

        for i in range(1, self.max_players+1):
            _temp_player_name = input(f'Введите имя игрока #{i}:')
            _temp_player_type = int(input(f'Введите тип игрока #{i} (человек = 1, компьютер = 0):'))
            _temp_player_game_name = 'Игрок' if _temp_player_type else 'Компьютер'

            self.players.append((_temp_player_type, Playing_Card(_temp_player_name, game_name=_temp_player_game_name)))

        self.barrel_bag.show_barrel()
        while len(self.barrel_bag.barrel_list) > 0:

            self.barrel_bag.show_barrel()
            print(f'\nСледующий бочонок: {self.barrel_bag.number} (осталось {len(self.barrel_bag.barrel_list)}) \n')
            for card in [card[1] for card in self.players]:
                card.open_card()

            _check = self._check()
            if isinstance(_check, PlayerException):
                print(_check.message + ' ' + _check.player)
                break
            elif _check is not None:
                if len(_check) > 1:
                    print(f'Ничья: {", ".join([p.name for p in _check])}')
                else:
                    print(f'Выйграл: {_check[0].name}')
                break


if __name__ == '__main__':
    Game.run_game()
