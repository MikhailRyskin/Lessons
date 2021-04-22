import random


class Warrior:

    def __init__(self, number):
        self.number = number
        self.health = 100

    #  по идее, этот метод должен принимать на вход объект Warrior
    #  Проверять, является ли он объектом класса Warrior и наносить урон ему, а не себе.
    #  Давайте немного поправим.
    def attack(self, unit):
        if isinstance(unit, Warrior):
            print(f'Атаковал воин {self.number}')
            unit.health -= 20
            print(f'У воина {unit.number} осталось {unit.health} здоровья')


unit_1 = Warrior(1)
unit_2 = Warrior(2)
lap = 0
while unit_1.health > 0 and unit_2.health > 0:
    lap += 1
    print(f'Раунд {lap}')
    choice = random.randint(1, 2)
    if choice == 1:
        unit_1.attack(unit_2)
    else:
        unit_2.attack(unit_1)
    print('_' * 20)
print(f'Игра окончена')
if unit_1.health > 0:
    print('Победу одержал воин 1')
else:
    print('Победу одержал воин 2')
