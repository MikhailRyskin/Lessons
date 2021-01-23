def sort_choice(my_list):
    for i_mn in range(len(my_list)):
        for i_curr in range(i_mn, len(my_list)):
            if my_list[i_curr] < my_list[i_mn]:
                my_list[i_curr], my_list[i_mn] = my_list[i_mn], my_list[i_curr]


rollers = int(input('Кол-во коньков: '))
rollers_list = []
for i in range(rollers):
    print('Размер', i + 1, 'пары:', end=' ')
    size = int(input())
    rollers_list.append(size)
people = int(input('Кол-во людей: '))
people_list = []
for i in range(people):
    print('Размер ноги', i + 1, 'человека:', end=' ')
    size = int(input())
    people_list.append(size)
sort_choice(rollers_list)
sort_choice(people_list)
people_count = 0
for man_size in people_list:
    for roller_size in rollers_list:
        if man_size <= roller_size:
            rollers_list.remove(roller_size)
            people_count += 1
            break
print('Наибольшее кол-во людей, которые могут взять ролики:', people_count)

# зачёт!
