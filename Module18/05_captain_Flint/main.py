def coordinates(coord):
    coord_list = coord.split()
    if coord_list[0] == 'West' or coord_list[0] == 'South':
        return -int(coord_list[1])
    else:
        return int(coord_list[1])


x_axis = input('По оси OX: ')
y_axis = input('По оси OY: ')
x = coordinates(x_axis)
y = coordinates(y_axis)
print(f'Координаты: x {x} y {y}')

# TODO, предлагаю реализовать функцию, которая проверяет, координаты и возвращает ответ.
#  Эту функцию применим к обоим переменным.
#  По оси OY: East 2
#  По оси OX: South 19
#  Координаты: 19 2
#  Должно получится: -19 2
# TODO функцию реализовал. По OY могут быть только север-юг, по  OX - восток-запад.
