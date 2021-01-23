main_list = [1, 5, 3]
list_b = [1, 5, 1, 5]
list_c = [1, 3, 1, 5, 3, 3]
main_list.extend(list_b)
count_5 = main_list.count(5)
ind = 0
while ind < len(main_list):
    if main_list[ind] == 5:
        main_list.remove(main_list[ind])
        ind -= 1
    else:
        ind += 1
main_list.extend(list_c)
print('Кол-во цифр 5 при первом объединении:', count_5)
print('Кол-во цифр 3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)

# зачёт!
