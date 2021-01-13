count = int(input('Кол-во контейнеров: '))
container_list = []
for _ in range(count):
    container = int(input('Введите вес контейнера: '))
    while container > 200:
        print('Вес контейнера больше 200!')
        container = int(input('Введите вес контейнера: '))
    container_list.append(container)
new_container = int(input('Введите вес нового контейнера: '))
while new_container > 200:
    print('Вес контейнера больше 200!')
    new_container = int(input('Введите вес нового контейнера: '))
position = 0
if new_container > container_list[0]:
    position = 1
elif new_container < container_list[-1]:
    position = count + 1
else:
    for i in range(count):
        if container_list[i] < new_container:
            position = i + 1
            break
print('Номер, куда встанет новый контейнер:', position)
