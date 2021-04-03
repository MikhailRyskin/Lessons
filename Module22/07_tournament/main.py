tour_1_file = open('first_tour.txt', 'r', encoding='utf8')
second_tour_ball = int(tour_1_file.readline())
second_tour_list = []

for line in tour_1_file:
    surname, name, ball = line[:-1].split()
    if int(ball) > second_tour_ball:
        second_tour_list.append((ball, f'{name[:1]}. {surname}'))

second_tour_quantity = len(second_tour_list)
second_tour_list.sort(reverse=True)
tour_2_file = open('second_tour.txt', 'a', encoding='utf8')
tour_2_file.write(f'{second_tour_quantity}\n')

for number, content in enumerate(second_tour_list):
    out_line = f'{number + 1}) {content[1]} {content[0]}\n'
    tour_2_file.write(out_line)
tour_1_file.close()
tour_2_file.close()
# зачёт!
