from itertools import chain


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade: int):
        if 0 < grade < 11:
            if isinstance(lecturer, Lecturer)\
                    and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def __average_grade(self):
        grades_list = list(self.grades.values())
        all_grades = list(map(int, chain.from_iterable(grades_list)))
        return round (sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя : {self.name}\nФамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.__average_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}\n"

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Операнд справа должен иметь тип Student')
        return self.__average_grade() == other.__average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Операнд справа должен иметь тип Student')
        return self.__average_grade() < other.__average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError('Операнд справа должен иметь тип Student')
        return self.__average_grade() > other.__average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def __average_grade(self):
        grades_list = list(self.grades.values())
        all_grades = list(map(int, chain.from_iterable(grades_list)))
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия : {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}"

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.__average_grade() == other.__average_grade()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.__average_grade() < other.__average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError('Операнд справа должен иметь тип Lecturer')
        return self.__average_grade() > other.__average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


student_1 = Student('Philip', 'Fry', 'male')
student_1.finished_courses = ['Donkey Kong']
student_1.courses_in_progress = ['english', 'algebra']
student_1.grades = {'Donkey Kong': [5], 'english': [2], 'algebra': [1]}

student_2 = Student('Leela', 'Turanga', 'female')
student_2.finished_courses = ['navigation']
student_2.courses_in_progress = ['english', 'algebra']
student_2.grades = {'navigation': [5], 'english': [4], 'algebra': [5]}

lecturer_1 = Lecturer('Hubert', 'Farnsworth')
lecturer_1.courses_attached = ['english']
lecturer_1.grades = {'english': [10]}

lecturer_2 = Lecturer('Ogden', 'Wernstrom')
lecturer_2.courses_attached = ['algebra']
lecturer_2.grades = {'algebra': [9]}

reviewer_1 = Reviewer('John', 'Zoidberg')
reviewer_1.courses_attached = ['english']
reviewer_1.courses_attached = ['algebra']

reviewer_2 = Reviewer('Amy', 'Wong')
reviewer_2.courses_attached = ['algebra', 'english']
reviewer_2.courses_attached = ['english', 'algebra']

student_1.rate_l(lecturer_1, 'english', 15)

reviewer_2.rate_hw(student_2, 'algebra', 4)

print(student_1 == student_2)
print(student_1 < student_2)
print(student_2 > student_1)

print(lecturer_1 == lecturer_2)
print(student_1 < student_2)
print(lecturer_2 > lecturer_1)

print(student_1)
print(lecturer_1)
print(reviewer_2)
