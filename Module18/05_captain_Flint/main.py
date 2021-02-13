y_axis = input('По оси OY: ').split()
x_axis = input('По оси OX: ').split()
x = int(x_axis[1])
y = int(y_axis[1])
if x_axis[0] == 'West':
    x = -x
if y_axis[0] == 'South':
    y = -y
print(f'Координаты: {x} {y}')
