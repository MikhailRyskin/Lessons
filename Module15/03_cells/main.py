n = int(input('Кол-во клеток: '))
cell_list = []
wrong_list = []
for i in range(n):
    print('Эффективность',  i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    if efficiency < i + 1:
        wrong_list.append(efficiency)
print('Неподходящие значения:', end=' ')
for k in wrong_list:
    print(k, end=' ')
