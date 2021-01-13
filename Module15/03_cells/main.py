cell_numbers = int(input('Кол-во клеток: '))
cell_list = []
wrong_list = []

# , Нейминг, предлагаю придумать более подходящие названия для переменных из одной буквы.
# , как нам рассчитать range таким образом, чтобы не пришлось делать вычисления с переменной "i"? =)
# TODO названия поменял, вычислений нет
for index in range(1, cell_numbers + 1):
    print('Эффективность', index, 'клетки:', end=' ')
    efficiency = int(input())
    if efficiency < index:
        wrong_list.append(efficiency)
print('Неподходящие значения:', end=' ')
for k in wrong_list:
    print(k, end=' ')
