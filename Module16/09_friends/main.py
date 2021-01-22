num_friends = int(input('Кол-во друзей: '))
num_receipts = int(input('Долговых расписок: '))
friends_list = []

# for _ in range(num_friends):
#     friends_list.append([0, 0])
# for ind in range(num_receipts):
#     print('\n', ind + 1, 'расписка:')
#     to_whom = int(input('Кому: '))
#     from_whom = int(input('От кого: '))
#     how_much = int(input('Сколько: '))
#     friends_list[to_whom - 1][1] += how_much
#     friends_list[from_whom - 1][1] -= how_much
# print('\nБаланс друзей:')
# for i in range(num_friends):
#     print(i + 1, ':', friends_list[i][1])

for _ in range(num_friends):
    friends_list.append(0)
for ind in range(num_receipts):
    print()
    print(ind + 1, 'расписка:')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_much = int(input('Сколько: '))
    friends_list[to_whom - 1] += how_much
    friends_list[from_whom - 1] -= how_much
print('\nБаланс друзей:')
for i in range(num_friends):
    print(i + 1, ':', friends_list[i])
