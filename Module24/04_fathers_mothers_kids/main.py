class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}', end=' ')
        if self.children:
            print('дети:', end='')
            for baby in self.children:
                print(baby.name, end=' ')
            print()
        else:
            print('детей нет')

    def calm_baby(self, baby):
        baby.calm = True
        print(f'родитель {self.name} успокоил(a) ребёнка {baby.name}')

    def feed_baby(self, baby):
        baby.fullness = True
        print(f'родитель {self.name} покормил(a) ребёнка {baby.name}')


class Baby:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm = False
        self.fullness = False

    def info(self):
        print(f'ребёнок: {self.name}, возраст: {self.age} успокоен {self.calm} сыт {self.fullness}')


father = Parent('Саша', 26)
mother = Parent('Маша', 25)
father.info()
mother.info()
baby = Baby('Петя', 2)
father.children.append(baby)
mother.children.append(baby)
father.info()
mother.info()
baby.info()
mother.feed_baby(baby)
father.calm_baby(baby)
baby.info()
