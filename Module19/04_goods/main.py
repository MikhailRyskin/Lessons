goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
codes_dict = {goods[item]: item for item in goods}
for code in store:
    total_quantity = 0
    value = 0
    # в этом цикле лучше идти сразу по store[code], без len.
    #  Это позволит сократить количество срезов.
    #  исправил
    for quantity_price in store[code]:
        total_quantity += quantity_price['quantity']
        value += quantity_price['quantity'] * quantity_price['price']
    print(f'{codes_dict[code]} - {total_quantity} шт., стоимость {value} руб.')

# зачёт!
