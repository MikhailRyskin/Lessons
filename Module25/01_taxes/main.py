class Property:
    def __init__(self, worth):
        self.worth = worth
        self.tax = 0

    def calc_tax(self):
        print(f'налог с суммы {self.worth} составит {self.tax}')


class Appartment(Property):
    def calc_tax(self):
        self.tax = self.worth / 1000
        super().calc_tax()


class Car(Property):
    def calc_tax(self):
        self.tax = self.worth / 200
        super().calc_tax()


class CountryHouse(Property):
    def calc_tax(self):
        self.tax = self.worth / 500
        super().calc_tax()


money = int(input('Сколько есть денег? '))
print('Налог на какое имущество: 1 - квартира, 2- машина, 3 - дача:', end=' ')
property_choice = int(input())
worth_object = int(input('Введите стоимость: '))
if property_choice == 1:
    tax_object = Appartment(worth_object)
elif property_choice == 2:
    tax_object = Car(worth_object)
elif property_choice == 3:
    tax_object = CountryHouse(worth_object)
tax_object.culc_tax()
tax = tax_object.tax
if money < tax:
    print('Вам не хватает', tax - money)
else:
    print('Денег хватает')
