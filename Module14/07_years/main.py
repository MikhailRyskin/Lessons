# def three_of_four(n):
#     dig1 = n // 1000
#     dig2 = (n // 100) % 10
#     dig3 = (n // 10) % 10
#     dig4 = n % 10
#     sample = dig1
#     count = 1
#     if dig2 == sample:
#         count += 1
#     if dig3 == sample:
#         count += 1
#     if dig4 == sample:
#         count += 1
#     if count == 3:
#         return True
#     else:
#         dig1, dig2 = dig2, dig1
#         sample = dig1
#         count = 1
#         if dig2 == sample:
#             count += 1
#         if dig3 == sample:
#             count += 1
#         if dig4 == sample:
#             count += 1
#         if count == 3:
#             return True
#         else:
#             return False

def three_of_four(year):
    sample = year[0]
    second = False
    for k in range(2):
        if second:
            sample = year[1]
        count = 0
        for symbol in year:
            if symbol == sample:
                count += 1
        if count == 3:
            return True
        second = True
    return False


a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))
print('Года от', a, 'до', b, 'с тремя одинаковыми цифрами:')
for year in range(a, b + 1):
    if three_of_four(str(year)):
        print(year)

# зачёт!
