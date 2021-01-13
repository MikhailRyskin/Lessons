# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for ind indn b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)

n = int(input('Введите размер списка: '))

list_1 = []

for _ in range(n):
    num = int(input('Введите число: '))
    list_1.append(num)

print('Изначальный список:', list_1)

while True:
    flag = True
    for i in range(n - 1):
        if list_1[i + 1] < list_1[i]:
            flag = False
            list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
    if flag:
        break
print('Отсортированный список:', list_1)

# зачёт!
