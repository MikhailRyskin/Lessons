ip_list = input('Введите IP: ').split('.')
digit_flag = False
flag_255 = False
wrong_elem = ''
for elem in ip_list:
    if not elem.isdigit():
        digit_flag = True
        wrong_elem = elem
        break
    elif int(elem) > 255:
        flag_255 = True
        wrong_elem = elem
        break

# , использовать переменную цикла после цикла не очень хорошая идея.
#  Если в цикл не попадём, то код выдаст ошибку.
#  Предлагаю создать переменную до цикла, равную пустой строке и в цикле работать с ней.
if len(ip_list) != 4:
    print('Адрес - это четыре числа, разделенные точками')
elif digit_flag:
    print(f'{wrong_elem} - не целое число')
elif flag_255:
    print(f'{wrong_elem} превышает 255')
else:
    print('IP-адрес корректен')

#  создал переменную.

# зачёт!
