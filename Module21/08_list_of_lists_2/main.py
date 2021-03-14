nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# такой параметр лишний, давайте сделаем его переменной в функции.
#  Чтобы пользователь не мог ввести параметр и сломать наш код
# def opening_list(in_list, new_list=[]):
#     for item in in_list:
#         if isinstance(item, list):
#             opening_list(item)
#         else:
#             new_list.append(item)
#     return new_list
#  убрал второй параметр

def opening_list(in_list):
    new_list = []
    for item in in_list:
        if isinstance(item, list):
            new_list += opening_list(item)
        else:
            new_list.append(item)
    return new_list


one_nice_list = opening_list(nice_list)
print(one_nice_list)

# зачёт!
