n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
row = ['I' for _ in range(n)]
for ind in range(1, k + 1):
    print('Бросок', ind, '. Сбиты палки с номера', end=' ')
    l_i = int(input(''))
    print('по номер', end=' ')
    r_i = int(input(''))
    row[l_i - 1:r_i] = '.' * (r_i - l_i + 1)
print(*row, sep='')

# TODO, пожалуйста, поправьте нейминг. Не очень, ясно, что такое l_i и r_i
#  озможно сможем решить задачу списковыми методами? =)