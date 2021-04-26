from random import randint, choice

ENLIGHTENMENT_CARMA_LEVEL = 500


class KillError(Exception):
    def __str__(self):
        return 'Kill'


class DrunkError(Exception):
    def __str__(self):
        return 'Drunk'


class CarCrashError(Exception):
    def __str__(self):
        return 'Car Crash'


class GluttonyError(Exception):
    def __str__(self):
        return 'Gluttony'


class DepressionError(Exception):
    def __str__(self):
        return 'Depression'


def one_day():
    dice = randint(1, 10)
    exceptions = [KillError, DrunkError, GluttonyError,
                  CarCrashError, DepressionError]
    if dice == 10:
        raise choice(exceptions)
    else:
        carma = randint(1, 7)
        return carma


total_carma = 0
day = 1

with open('karma.log', 'w+', encoding='utf8') as log_file:
    while total_carma < ENLIGHTENMENT_CARMA_LEVEL:
        try:
            total_carma += one_day()
        except (KillError, DrunkError, CarCrashError,
                GluttonyError, DepressionError) as exc:
            except_content = f'день {day:>4} {str(exc)}\n'
            log_file.write(except_content)
        day += 1

print(f'день {day}, карма {total_carma}!!!')
