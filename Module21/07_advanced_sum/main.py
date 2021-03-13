def opening_list(in_list, new_list=[]):
    for item in in_list:
        if isinstance(item, list):
            opening_list(item)
        else:
            new_list.append(item)
    return new_list


def my_sum(in_list):
    open_list = opening_list(in_list)
    summ = sum(open_list)
    open_list.clear()
    return summ


list_1 = [[1, 2, [3]], [1], 3]
print(my_sum(list_1))

list_2 = (1, 2, 3, 4, 5)
print(my_sum(list_2))
