class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Имя: {self.__name} Фамилия: {self.__surname} Возраст: {self.__age}'


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0

    def salary_calc(self):
        self.salary = 0

    def __str__(self):
        info = super().__str__()
        info = ' '.join((info, f'Заработная плата: {self.salary}'))
        return info


class Manager(Employee):
    def salary_calc(self):
        self.salary = 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.sales_volume = sales_volume

    def salary_calc(self):
        self.salary = 5000 + self.sales_volume * 0.05


class Worker(Employee):
    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.hours_worked = hours_worked

    def salary_calc(self):
        self.salary = 100 * self.hours_worked


persons = [Manager('Андрей', 'Лунёв', 29), Manager('Михаил', 'Кержаков', 32), Manager('Александр', 'Васютин', 25),
           Agent('Дуглас', 'Сантос', 28, 5000), Agent('Деян', 'Ловрен', 32, 3000), Agent('Юрий', 'Жирков', 38, 6000),
           Worker('Вильмар', 'Барриос', 29, 500), Worker('Сердар', 'Азмун', 26, 60), Worker('Артем', 'Дзюба', 32, 1000),
           ]
for person in persons:
    person.salary_calc()
    print(person)

# зачёт!
