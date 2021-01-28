n = int(input('Введите длину списка: '))
my_list = [(1 if ind % 2 == 0 else ind % 5) for ind in range(n)]
print('Результат:', my_list)

# зачёт!
