n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
row = ['I' for _ in range(n)]
for ind in range(1, k + 1):
    print('Бросок', ind, '. Сбиты палки с номера', end=' ')
    left_ind = int(input(''))
    print('по номер', end=' ')
    right_ind = int(input(''))
    row[left_ind - 1:right_ind] = '.' * (right_ind - left_ind + 1)
print(*row, sep='')

# , пожалуйста, поправьте нейминг. Не очень, ясно, что такое l_i и r_i
# TODO поправил
#  озможно сможем решить задачу списковыми методами? =)
# TODO не очень понимаю, какие списковые методы упростят решение