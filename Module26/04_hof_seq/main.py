from collections.abc import Iterable


def hof_seq(number_1: int, number_2: int, number_members: int) -> Iterable:
    if number_1 == 1 and number_2 == 1:
        seq_list = []
        seq_index = 0
        while seq_index < number_members:
            if seq_index == 0 or seq_index == 1:
                seq_member = 1
            else:
                seq_member = seq_list[seq_index - seq_list[seq_index - 1]]\
                             + seq_list[seq_index - seq_list[seq_index - 2]]
            seq_list.append(seq_member)
            yield seq_member
            seq_index += 1
    else:
        print('Неверные начальные члены последовательности')
        return


member_1 = 1
member_2 = 1
number_members = 20
hof = hof_seq(member_1, member_2, number_members)
print(f'Последовательность Хофштадтера для {number_members} членов последовательности:')
for elem in hof:
    print(elem, end=' ')
