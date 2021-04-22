import random


class Student:

    def __init__(self, name, group_number, achievement):
        self.name = name
        self.group_number = group_number
        self.achievement = achievement
        self.average_score = round(sum(achievement) / len(achievement), 2)

    def info(self):
        print(f'Студент {self.name} группа {self.group_number} средний балл {self.average_score}')


names = ['Иванов', 'Петров', 'Сидоров', 'Дзюба', 'Ловрен', 'Барриос', 'Кузяев', 'Лунёв', 'Кержаков', 'Азмун']
students = []
for name in names:
    group = random.randint(100, 105)
    points = [random.randint(2, 5) for _ in range(5)]
    student = Student(name, group, points)
    students.append(student)
student_list = []
for student in students:
    student_list.append((student.average_score, student.name, student.group_number))

#  Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" не отражает. "i" это же студент? =)
for student in sorted(student_list):
    print(f'студент {student[1]} группа {student[2]} средний балл {student[0]}')

# зачёт!
