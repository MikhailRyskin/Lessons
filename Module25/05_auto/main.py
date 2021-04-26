from math import cos, sin


class Auto:
    def __init__(self, x, y, move_direction):
        self.x = x
        self.y = y
        self.move_direction = move_direction

    def __str__(self):
        return f'ТС находится в координатах: x={self.x}, y={self.y}, направление {self.move_direction}'

    def move(self, distance):
        print(f'движение на {distance} в направлении {self.move_direction}')
        self.x += distance * cos(self.move_direction)
        self.y += distance * sin(self.move_direction)

    def new_direction(self, direction):
        self.move_direction = direction
        print(f'направление движения изменено на {self.move_direction}')


class Bus(Auto):
    def __init__(self, x, y, move_direction):
        super().__init__(x, y, move_direction)
        self.number_passengers = 0
        self.received_money = 0

    def __str__(self):
        info = super().__str__()
        info = '\n'.join((info, f'в автобусе {self.number_passengers} пассажиров,'
                                f' получено денег {self.received_money}'))
        return info

    def get_on_bus(self, quantity):
        print(f'вошло пассажиров:{quantity} ')
        self.number_passengers += quantity

    def get_off_bus(self, quantity):
        print(f'вышло пассажиров:{quantity} ')
        self.number_passengers -= quantity

    def move(self, distance):
        super().move(distance)
        self.received_money += self.number_passengers * distance * 0.1
        print(f'за перевозку на {distance} км {self.number_passengers} пассажиров будет получено {self.received_money}')


uaz = Auto(10, 20, 2)
print(uaz)
uaz.move(100)
print(uaz)
uaz.new_direction(1)
print(uaz)

bus_9 = Bus(20, 30, 1.5)
print(bus_9)
bus_9.get_on_bus(23)
print(bus_9)
bus_9.get_off_bus(12)
print(bus_9)
bus_9.move(100)
print(bus_9)
