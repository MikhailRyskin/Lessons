from collections.abc import Iterable


class SquareIterator:
    def __init__(self, number: int) -> None:
        self.counter = 0
        self.number = number

    def __iter__(self) -> None:  # TODO, в данном случае, было бы правильней возвращать 'SquareIterator'
        self.counter = 0
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter > self.number:
            raise StopIteration
        return self.counter ** 2


def square_generator(range_number: int) -> Iterable:
    for number in range(1, range_number + 1):
        yield number ** 2


input_range = int(input('Введите границу диапазона чисел: '))
print(f'Квадраты чисел от 1 до {input_range}')

my_iterator = SquareIterator(input_range)
for num in my_iterator:
    print(num, end=' ')

print()
my_generator = square_generator(input_range)
for num in my_generator:
    print(num, end=' ')

print()
generator = (num ** 2 for num in range(1, input_range + 1))
for num in generator:
    print(num, end=' ')
