class Potato:

    stages = {0: 'посажена', 1: 'росток', 2: 'зелёная', 3: 'созрела'}

    def __init__(self, number):
        self.number = number
        self.stage = 0

    def info(self):
        print(f'Картошка {self.number} сейчас {Potato.stages[self.stage]}')

    def grow(self):
        if self.stage < 3:
            self.stage += 1
        self.info()

    def is_ripe(self):
        return self.stage >= 3


class PotatoGarden:

    def __init__(self, count):
        self.potato_list = [Potato(i) for i in range(1, count + 1)]

    def are_all_ripe(self):
        if not all([potato.is_ripe() for potato in self.potato_list]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def grow_garden(self):
        print('Картошка прорастает!')
        for potato in self.potato_list:
            potato.grow()


class Gardener:

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def handle_garden(self):
        print(f'садовник {self.name} ухаживает за грядкой')
        self.garden.grow_garden()

    def harvest(self):
        self.garden = []
        print(f'садовник {self.name} собрал урожай')
