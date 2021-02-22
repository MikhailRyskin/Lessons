customer_dict = {}
num_orders = int(input('Введите кол-во заказов: '))
for i in range(1, num_orders + 1):
    order_list = input(f'{i} заказ: ').split()
    if not order_list[0] in customer_dict:
        customer_dict[order_list[0]] = {}
        customer_dict[order_list[0]][order_list[1]] = int(order_list[2])
    elif not order_list[1] in customer_dict[order_list[0]]:
        customer_dict[order_list[0]][order_list[1]] = int(order_list[2])
    else:
        customer_dict[order_list[0]][order_list[1]] += int(order_list[2])
print(customer_dict)
for name in sorted(customer_dict.keys()):
    print(name, ':')
    for pizza in sorted(customer_dict[name].keys()):
        print(f'   {pizza}: {customer_dict[name][pizza]}')
