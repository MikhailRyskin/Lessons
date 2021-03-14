def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number - 1)


def calculating_math_func(data):
    result = factorial(data)
    result /= data ** 3
    result = result ** 10
    return result


input_number = int(input('Введите число: '))
print(calculating_math_func(input_number))

# зачёт!
