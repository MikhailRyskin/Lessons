
# TODO, давайте подумаем, как сократить количество условных операторов в коде
def three_offour(n):
    dig1 = n // 1000
    dig2 = (n // 100) % 10
    dig3 = (n // 10) % 10
    dig4 = n % 10
    sample = dig1
    count = 1
    if dig2 == sample:
        count += 1
    if dig3 == sample:
        count += 1
    if dig4 == sample:
        count += 1
    if count == 3:
        return True
    else:
        dig1, dig2 = dig2, dig1
        sample = dig1
        count = 1
        if dig2 == sample:
            count += 1
        if dig3 == sample:
            count += 1
        if dig4 == sample:
            count += 1
        if count == 3:
            return True
        else:
            return False


a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))
print('Года от', a, 'до', b, 'с тремя одинаковыми цифрами:')
for year in range(a, b + 1):
    if three_offour(year):
        print(year)
