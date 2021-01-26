alphabet = 'abcdefg'

print('1. Копия строки:', alphabet[:])
print('2. Элементы строки в обратном порядке:', alphabet[::-1])
print('3. Каждый второй элемент строки (включая самый первый):', alphabet[::2])
print('4. Каждый второй элемент строки после первого:', alphabet[1::2])
print('5. Все элементы до второго:', alphabet[0])
print('6. Все элементы начиная с конца до предпоследнего:', alphabet[-1])
print('7. Все элементы в диапазоне индексов от 3 до 4 (не включая 4):', alphabet[3])
print('8. Последние три элемента строки:', alphabet[-3:])
print('9. Все элементы в диапазоне индексов от 3 до 4 (не включая 5):', alphabet[3:5])
print('10. То же, что и в предыдущем, но выводится в обратном порядке:', alphabet[4:2:-1])
