import re

if __name__ == '__main__':
    plates = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

    private_car_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b')
    taxi_pattern = re.compile(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b')

    private_cars = re.findall(private_car_pattern, plates)
    taxi = re.findall(taxi_pattern, plates)
    print('Список номеров частных автомобилей:', private_cars)
    print('Список номеров такси:', taxi)

# зачёт!
