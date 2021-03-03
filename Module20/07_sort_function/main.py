def tuple_sorted(input_tuple):
    for number in input_tuple:
        if number % 1 != 0:
            return input_tuple
    new_list = list(input_tuple)
    new_list.sort()
    sort_tuple = tuple(new_list)
    return sort_tuple


my_tuple = (23, 45, 2, 56, -127, 15, 4, 76, 1, -3)
# my_tuple = (23, 45, 2, 56.54, 4, 76, 1, -3)

my_sort_tuple = tuple_sorted(my_tuple)
print(my_sort_tuple)

# зачёт!
