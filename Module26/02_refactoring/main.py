from collections.abc import Iterable

list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


# can_continue = True
# for x in list_1:
#     for y in list_2:
#         result = x * y
#         print(x, y, result)
#         if result == to_find:
#             print('Found!!!')
#             can_continue = False
#             break
#     if not can_continue:
#         break


def my_generator(list_1: list, list_2: list, to_find: int) -> Iterable:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield x, y, result
            if result == to_find:
                print('Found!!!')
                return


gen = my_generator(list_1, list_2, to_find)
for x, y, result in gen:
    print(x, y, result)

# зачёт!
