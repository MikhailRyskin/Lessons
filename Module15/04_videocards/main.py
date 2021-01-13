count = int(input('Кол-во видеокарт: '))
models_list = []

for i in range(count):
    print(i + 1, 'Видеокарта: ', end='')
    model = int(input())
    models_list.append(model)

print('Старый список видеокарт:', models_list)

new_model = models_list[0]

for card in models_list:
    if card > new_model:
        new_model = card
updated_list = []

for card in models_list:
    if card != new_model:
        updated_list.append(card)
print('Новый список видеокарт:', updated_list)

# зачёт!
