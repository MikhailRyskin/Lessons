import random


class Warrior:

    def __init__(self, number):
        self.number = number
        self.health = 100

    def action(self, attack):
        if attack:
            print(f'Атаковал воин {self.number}')
        else:
            self.health -= 20
            print(f'У воина {self.number} осталось {self.health} здоровья')


choice_list = [True, False]
unit_1 = Warrior(1)
unit_2 = Warrior(2)
lap = 0
while unit_1.health > 0 and unit_2.health > 0:
    lap += 1
    print(f'Раунд {lap}')
    choice = random.choice(choice_list)
    unit_1.action(choice)
    unit_2.action(not choice)
    print('_' * 20)
print(f'Игра окончена')
if unit_1.health > 0:
    print('Победу одержал воин 1')
else:
    print('Победу одержал воин 2')
