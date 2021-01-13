n = int(input('Кол-во клеток: '))
cell_list = []
wrong_list = []

# TODO, Нейминг, предлагаю придумать более подходящие названия для переменных из одной буквы.
# TODO, как нам рассчитать range таким образом, чтобы не пришлось делать вычисления с переменной "i"? =)
for i in range(n):
    print('Эффективность', i + 1, 'клетки:', end=' ')
    efficiency = int(input())
    if efficiency < i + 1:
        wrong_list.append(efficiency)
print('Неподходящие значения:', end=' ')
for k in wrong_list:
    print(k, end=' ')
