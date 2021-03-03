def interests_surnames_length(stud_dict):
    interests_list = []
    total_surnames_length = 0
    for stud_data in stud_dict.values():
        interests_list.extend(stud_data['interests'])
        total_surnames_length += len(stud_data['surname'])
    return interests_list, total_surnames_length


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
# print(pairs)
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

for students_id, students_data in students.items():
    students_age = students_data['age']
    print(f'ID студента: {students_id} возраст студента: {students_age}')

students_interests, surnames_length = interests_surnames_length(students)
print('Полный список интересов всех студентов:', students_interests)
print('Общая длина всех фамилий студентов:', surnames_length)

# зачёт!
# зачёт!
