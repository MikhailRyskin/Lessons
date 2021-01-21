def sort_choice(my_list):
    for i_mn in range(len(my_list)):
        for i_curr in range(i_mn, len(my_list)):
            if my_list[i_curr] < my_list[i_mn]:
                my_list[i_curr], my_list[i_mn] = my_list[i_mn], my_list[i_curr]


class_1 = list(range(160, 177, 2))
class_2 = list(range(162, 181, 3))
class_1.extend(class_2)
sort_choice(class_1)
print('Отсортированный список:', class_1)
