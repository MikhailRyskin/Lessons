shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

item = input('Название детали: ')
items_count = 0
items_amount = 0
for ind in range(len(shop)):
    if shop[ind][0] == item:
        items_count += 1
        items_amount += shop[ind][1]
print('Кол-во деталей -', items_count)
print('Общая стоимость -', items_amount)

# зачёт!
