text = input('Введите слово: ')
text_list = list(text)
middle = len(text_list) // 2
left = []
right = []
for i in range(middle):
    left.append(text_list[i])
for i in range(-1, -(middle + 1), -1):
    right.append(text_list[i])
print(left, right)
if left == right:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')
