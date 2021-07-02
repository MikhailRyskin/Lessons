from collections.abc import Iterable
from typing import List


def hof_seq(input_list: List[int], sequence_length: int) -> Iterable:
    #  пожалуйста, обратите внимание, на вход Генератор должен получать список из двух элементов.
    #  Предлагаю попробовать запускать цикл while вне условного оператора, только в том случае,
    #  если мы не вышли из функции при помощи return.
    #  Таким образом, немного разделим код на части, что улучшит его читаемость.
    if input_list[0] != 1 or input_list[1] != 1:
        print('Неверные начальные члены последовательности')
        return

    seq_list = []
    seq_index = 0
    while seq_index < sequence_length:
        if seq_index == 0 or seq_index == 1:
            seq_member = 1
        else:
            seq_member = seq_list[seq_index - seq_list[seq_index - 1]] \
                         + seq_list[seq_index - seq_list[seq_index - 2]]
        seq_list.append(seq_member)
        yield seq_member
        seq_index += 1


start_list = [1, 1]
number_members = 20
hof = hof_seq(start_list, number_members)
print(f'Последовательность Хофштадтера для {number_members} членов последовательности:')
for elem in hof:
    print(elem, end=' ')

# зачёт!
