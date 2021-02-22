customer_dict = {}
num_orders = int(input('Введите кол-во заказов: '))
#  Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i" не отражает =)
#  TODO исправил название переменной
for i_order in range(1, num_orders + 1):
    order_list = input(f'{i_order} заказ: ').split()
    customer_name = order_list[0]
    pizza_name = order_list[1]
    number_pizzas = order_list[2]

    #  для сокращения количества срезов, предлагаю сохранить в переменную результат выполнения order_list[0] и т.д.
    #  и далее в коде работать с переменными.
    #  TODO сохранил в переменные
    if customer_name not in customer_dict:
        customer_dict[customer_name] = {}
        customer_dict[customer_name][pizza_name] = int(number_pizzas)
    elif pizza_name not in customer_dict[customer_name]:
        customer_dict[customer_name][pizza_name] = int(number_pizzas)
    else:
        customer_dict[customer_name][pizza_name] += int(number_pizzas)
print(customer_dict)
for name in sorted(customer_dict.keys()):
    print(name, ':')
    for pizza in sorted(customer_dict[name].keys()):
        print(f'   {pizza}: {customer_dict[name][pizza]}')
