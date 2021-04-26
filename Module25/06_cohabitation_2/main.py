from termcolor import cprint
from random import randint


class House:
    total_food_eaten = 0
    total_money_earned = 0
    total_fur_coats = 0

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30
        self.house_cat = None
        self.resident = []

    def __str__(self):
        return 'В доме: еда  {}, деньги  {}, грязь  {}, кошачий корм {}'.format(
            self.food, self.money, self.dirt, self.cat_food
        )


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None

    def __str__(self):
        return '{}, сытость {}, счастье {}'.format(self.name, self.fullness, self.happiness)

    def eat(self, portion_food):
        if self.house.food >= portion_food:
            cprint('{} - приём пищи'.format(self.name), color='green')
            self.fullness += portion_food
            self.house.food -= portion_food
            House.total_food_eaten += portion_food
        else:
            self.fullness -= 10
            cprint('{} нет еды'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        house.resident.append(self)
        cprint('{} - заселение в дом'.format(self.name), color='green')

    def pick_up_cat(self, cat, house):
        self.house.house_cat = cat
        cat.house = house
        house.resident.append(cat)
        cprint('{}: У нас есть кот! Зовут {}'.format(self.name, cat.name), color='cyan')

    def petting_cat(self, cat):
        self.fullness -= 10
        self.happiness += 5
        cprint('{} - ласки кота! Кот {}'.format(self.name, cat.name), color='green')

    def act(self):
        if self.house.dirt > 90:
            self.happiness -= 10
        self.house.dirt += 5


class Husband(Man):

    def __str__(self):
        return 'Муж - ' + super().__str__()

    def act(self):
        super().act()
        if self.fullness <= 0 or self.happiness < 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat(30)
        elif self.house.money < 60:
            self.work()
        elif dice == 1 or dice == 2:
            self.gaming()
        elif dice == 3:
            self.petting_cat(self.house.house_cat)
        else:
            self.work()

    def work(self):
        self.fullness -= 10
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        House.total_money_earned += 150

    def gaming(self):
        self.fullness -= 10
        cprint('{} играл в "Танки" целый день'.format(self.name), color='green')
        self.happiness += 10


class Wife(Man):

    def __str__(self):
        return 'Жена - ' + super().__str__()

    def act(self):
        super().act()
        if self.fullness <= 0 or self.happiness < 10:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 30:
            self.eat(30)
        elif self.house.food <= 60:
            self.shopping()
        elif self.house.dirt > 100:
            self.clean_house()
        elif self.house.cat_food <= 20:
            self.buying_cat_food()
        elif dice == 1:
            self.buy_fur_coat()
        else:
            self.petting_cat(self.house.house_cat)

    def shopping(self):
        self.fullness -= 10
        if self.house.money >= 90:
            cprint('{} сходила в магазин за едой'.format(self.name), color='blue')
            self.house.money -= 90
            self.house.food += 90
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buying_cat_food(self):
        self.fullness -= 10
        if self.house.money >= 40:
            cprint('{} купила кошачий корм'.format(self.name), color='blue')
            self.house.money -= 40
            self.house.cat_food += 40
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.house.money >= 450:
            cprint('{} купила шубу!!!'.format(self.name), color='cyan')
            self.house.money -= 350
            self.happiness += 60
            House.total_fur_coats += 1
        else:
            cprint('{} "Нет денег на шубу!"'.format(self.name), color='red')

    def clean_house(self):
        self.fullness -= 20
        cprint('{} сделала уборку в доме'.format(self.name), color='blue')
        if self.house.dirt > 100:
            self.house.dirt -= 100
        else:
            self.house.dirt = 0

    def __add__(self, other):
        if isinstance(other, Husband):
            cprint('{} и {} стали родителями! Надо придумать имя ребёнка.'.format(
                self.name, other.name), color='cyan')
            return Child(name=None)
        else:
            return None


class Cat:

    def __init__(self, name):
        self.fullness = 30
        self.house = None
        self.name = name

    def __str__(self):
        return 'Кот - {}, сытость {}'.format(self.name, self.fullness)

    def cat_eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот поел', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('Нет кошачьей еды', color='red')
            self.fullness -= 10

    def cat_sleep(self):
        cprint('Кот спал', color='yellow')
        self.fullness -= 10

    def tear_up_wallpaper(self):
        cprint('Кот драл обои!', color='yellow')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('Кот умер!!!', color='red')
            return
        dice = randint(1, 3)
        if self.fullness < 20:
            self.cat_eat()
        elif dice == 1:
            self.tear_up_wallpaper()
        else:
            self.cat_sleep()


class Child(Man):

    def __str__(self):
        return 'Ребёнок - ' + super().__str__()

    def act(self):
        self.house.dirt += 5
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 15:
            self.eat(10)
        else:
            self.sleep()

    def sleep(self):
        self.fullness -= 10
        cprint('{} спал'.format(self.name), color='green')


serge = Husband(name='Сережа')
masha = Wife(name='Маша')
my_sweet_home = House()
serge.go_to_the_house(my_sweet_home)
masha.go_to_the_house(my_sweet_home)
barsik = Cat(name='Барсик')
masha.pick_up_cat(barsik, my_sweet_home)

kid = masha + serge
kid.name = 'Петя'
kid.go_to_the_house(my_sweet_home)

print('В доме живут:')
for roomer in my_sweet_home.resident:
    cprint(roomer.name, color='yellow')
print(my_sweet_home)
print()

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='magenta')
    for roomer in my_sweet_home.resident:
        roomer.act()
    cprint('---------------- в конце дня ----------------', color='magenta')
    for roomer in my_sweet_home.resident:
        print(roomer)
    print(my_sweet_home)

cprint('\nВсего съедено еды {}'.format(House.total_food_eaten), color='magenta')
cprint('Всего заработано денег {}'.format(House.total_money_earned), color='magenta')
cprint('Всего куплено шуб {}'.format(House.total_fur_coats), color='magenta')
