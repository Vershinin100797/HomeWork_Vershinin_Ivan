import os
import shutil


def select_dir():
    path = input('Введите адрес директории: ')
    if os.path.isdir(path):
        os.chdir(path)
        print(f'Вы перешли в директорию \'{path}\'.')
    else:
        print('Такой директории не существует!')


def dir_list():
    print(os.listdir('.'))


def mk_dir():
    dir_name = input('Введите название новой папки: ')
    try:
        os.mkdir(dir_name)
        print(f'Папка \'{dir_name}\' успешно создана!')
    except OSError:
        print(f'Папка \'{dir_name}\' уже существует!')


def rm_dir():
    dir_name = input('Введите название папки, которую хотите удалить: ')
    if dir_name in os.listdir('.'):
        if os.path.isdir(dir_name):
            shutil.rmtree(dir_name)
            print(f'Папка \'{dir_name}\' успешно удалена!')
        else:
            print(f'Удаление не возможно! \'{dir_name}\' не является папкой.')
    else:
        print(f'Папки \'{dir_name}\' не существует!')