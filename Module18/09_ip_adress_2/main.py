ip_list = input('Введите IP: ').split('.')
digit_flag = False
flag_255 = False
for elem in ip_list:
    if not elem.isdigit():
        digit_flag = True
        break
    elif int(elem) > 255:
        flag_255 = True
        break

# TODO, использовать переменную цикла после цикла не очень хорошая идея.
#  Если в цикл не попадём, то код выдаст ошибку.
#  Предлагаю создать переменную до цикла, равную пустой строке и в цикле работать с ней.
if len(ip_list) != 4:
    print('Адрес - это четыре числа, разделенные точками')
elif digit_flag:
    print(f'{elem} - не целое число')
elif flag_255:
    print(f'{elem} превышает 255')
else:
    print('IP-адрес корректен')
