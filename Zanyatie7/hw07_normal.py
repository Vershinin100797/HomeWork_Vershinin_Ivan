__author__ = 'Вершинин Иван Александрович'
# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class School(object):
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    @property
    def name(self):
        return self._school_name

    @property
    def adress(self):
        return self._school_adress


class People(object):
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return f'{self._last_name} {self._first_name} {self._middle_name}'
    @property
    def get_short_name(self):
        return f'{self._last_name} {self._first_name[:1]}.{self._middle_name[:1]}.'
                                     


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mother, father):
        super().__init__(last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mother': mother,
            'father': father
            }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        super().__init__(last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


if __name__ == '__main__':

    teachers = [
        Teacher('Иванов', 'Иван', 'Иванович', 'Математика',
                ['2B', '1A']),
        Teacher('Петров', 'Петр', 'Петрович', 'Русский язык',
                ['3A', '2B'])]


    students = [
        Student('Борисов', 'Борис', 'Борисович', '1A', 'Борисова А.В.', 'Борисов Б.А.'),
        Student('Сидоров', 'Виталий', 'Петрович', '2B', 'Сидорова Т.М.', 'Сидоров П.В.'),
        Student('Семенов', 'Василий', 'Иванович', '1A', 'Семенова А.К.', 'Семенов И.Г.'),
        Student('Полищук', 'Николай', 'Александрович', '3A', 'Полищук С.М.', 'Полищук С.Ф.')]

    school = School('Начальная школа №1', 'Тольятти', teachers, students)

    print(f'Название школы:\n{school.name}')
    print(f'Адрес школы:\n{school.adress}')

    print(f'\nСписок всех классов:\n{", ".join(school.get_all_classes())}')
    print('\nСписок учеников в "1A" классе:{}'.format('\n'.join(school.get_students("1A"))))

    student = school.find_student('Полищук Николай Александрович')
    print(f'\nУченик: {student["full_name"]}\nКласс: "{student["class_room"]}"\
        \nПреподаватель: {", ".join(student["teachers"])}\
        \nПердмет: {", ".join(student["lessons"])}')

    print(f'\nРодители: {student["parents"]["mother"]}, {student["parents"]["father"]}')

    print(f'\nКласс: "1А"\nПреподаватель: {", ".join(school.get_teachers("1A"))}')