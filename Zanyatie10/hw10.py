__author__ = 'Вершинин Иван Александрович'


class University(object):

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.students_list = []
        self.group_list = []

    # добавление нового студента
    def add_students(self, s_data):
        _student = Students(**s_data)
        if _student not in self.students_list:
            self.students_list.append(_student)

    # создание новой группы
    def create_group(self, g_name):
        if g_name not in self.group_list:
            self.group_list.append(g_name)

    # получение списка всех групп
    def get_all_groups(self):
        _group_list = list(set([student.get_group for student in self.students_list]))
        for group_item in self.group_list:
            if group_item not in _group_list:
                _group_list.append(group_item)
        return _group_list

    def _get_headmans_list(self):
        headmans_list = []
        for headmans_item in self.students_list:
            if headmans_item.get_headman == 'Староста':
                headmans_list.append({
                     'headman_fio': headmans_item.get_fio,
                     'headmen_group': headmans_item.get_group
                })
        return headmans_list

    # поиск всех старост
    def get_headmans(self):
        headmans = self._get_headmans_list()
        print('Список старост:')
        for i in headmans:
            print(f'ФИО: {i["headman_fio"]}, группа: {i["headmen_group"]}')

    # Список студентов в группе
    def get_students_in_group(self, group):
        return [student.get_fio for student in self.students_list if
                group == student.get_group]

    # Поиск студента по имени
    def find_student(self, student_full_name):
        for person in self.students_list:
            if student_full_name == person.get_full_name:
                return {
                    'fio': person.get_fio,
                    'student_id': person.get_st_id,
                    'group': person.get_group,
                    'date_of_birth': person.get_dob,
                    'headman': person.get_headman,
                    'code': person.get_code,
                    'telephone': person.get_phone
                }
            else:
                print('Студентов с таким именем нет!')

    # Отчисление студента (по уникальному id)
    def rm_student(self, student_unique_id):
        for person in self.students_list:
            if student_unique_id == person.get_st_id:
                self.students_list.remove(person)
                print('Студент отчислен')
            else:
                print('Студентов с таким id нет!')


class People(object):

    last_name = None
    first_name = None
    middle_name = None
    date_of_birth = None
    phone = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    @property
    def get_dob(self):
        return self.date_of_birth

    @property
    def get_phone(self):
        return self.phone


class Students(People):
    st_id = None
    group = None
    code = None
    headman = False

    def __init__(self, **kwargs):
        super(Students, self).__init__(**kwargs)
        self.__dict__.update(kwargs)

    @property
    def get_fio(self):
        return f'{self.last_name} {self.first_name[:1]}. {self.middle_name[:1]}.'

    @property
    def get_st_id(self):
        return self.st_id

    @property
    def get_group(self):
        return self.group

    @property
    def get_headman(self):
        if self.headman:
            return 'Староста'
        else:
            return 'Студент'

    @property
    def get_code(self):
        return self.code


if __name__ == '__main__':

    new_student = {'last_name': 'Борисов',
                   'first_name': 'Борис',
                   'middle_name': 'Борисович',
                   'st_id': '1A13',
                   'date_of_birth': '10.07.1993',
                   'phone': 88005553535,
                   'group': 'ПМ-1232',
                   'headman': True,
                   'code': 230685}
    new_student2 = {'last_name': 'Иванов',
                    'first_name': 'Иван',
                    'middle_name': 'Иванович',
                    'st_id': '1234',
                    'date_of_birth': '12.02.1993',
                    'phone': 88005553535,
                    'group': 'АМ-1327',
                    'headman': True,
                    'code': '230421'}
    new_student3 = {'last_name': 'Воронцов',
                    'first_name': 'Петр',
                    'middle_name': 'Алексеевич',
                    'st_id': '3D21',
                    'date_of_birth': '20.04.1996',
                    'phone': 88005553535,
                    'group': 'ВТ-1911',
                    'headman': False,
                    'code': 230642}

    university = University()
    university.add_students(new_student)
    university.add_students(new_student2)
    university.add_students(new_student3)
    university.create_group('ВТ-1931')

    # вызов метода отчисления студента
    # university.rm_student('3D21')

    print(f'\nСписок групп:\n{", ".join(university.get_all_groups())}')
    print('\nСписок студентов в группе "ПМ-1232": \n{}'.format('\n'.join(university.get_students_in_group("ПМ-1232"))))

    university.get_headmans()

    student = university.find_student('Борисов Борис Борисович')

    print(f'\nСтудент: {student["fio"]}\
         \nУникальный идентификатор студента: {student["student_id"]}\
         \nГруппа: {student["group"]}\
         \nДата рождения: {student["date_of_birth"]}\
         \nСтароста: {student["headman"]}\
         \nКод специальности: {student["code"]}\
         \nТелефон: {student["telephone"]}')
