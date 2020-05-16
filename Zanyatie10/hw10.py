__author__ = 'Вершинин Иван Александрович'


class University(object):
    def __init__(self, students):
        self._students = students

    def get_all_groups(self):
        return list(set([student.get_group for student in self._students]))

    def get_students(self, group):
        return [student.get_fio for student in self._students if
                group == student.get_group]

    def find_student(self, student_full_name):
        for person in self._students:
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


class People(object):
    def __init__(self, last_name, first_name, middle_name, dob, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.dob = dob
        self.phone = phone

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    @property
    def get_dob(self):
        return self.dob

    @property
    def get_phone(self):
        return self.phone


class Students(People):
    def __init__(self, last_name, first_name, middle_name, st_id, dob, phone, group, headman, code):
        super(Students, self).__init__(last_name, first_name, middle_name, dob, phone)
        self.st_id = st_id
        self.group = group
        self.headman = headman
        self.code = code

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

    students = [
        Students('Борисов', 'Борис', 'Борисович', '1A13', '10.07.1993', '88005553535', 'ПМ-1232', 1, '230685'),
        Students('Полищук', 'Иван', 'Петрович', '3A41', '14.09.1994', '88082132456', 'ПМ-1234', 1, '321254')]

    university = University(students)

    print(f'\nСписок групп:\n{", ".join(university.get_all_groups())}')
    print('\nСписок учеников в группе "ПМ-1232": {}'.format('\n'.join(university.get_students("ПМ-1232"))))

    student = university.find_student('Полищук Иван Петрович')
    print(f'\nСтудент: {student["fio"]}\
         \nУникальный идентификатор студента: {student["student_id"]}\
         \nГруппа: {student["group"]}\
         \nДата рождения: {student["date_of_birth"]}\
         \nСтароста: {student["headman"]}\
         \nКод специальности: {student["code"]}\
         \nТелефон: {student["telephone"]}')
