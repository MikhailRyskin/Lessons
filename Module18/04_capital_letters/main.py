text_list = input('Введите строку: ').split()
result = ' '.join([word.title() for word in text_list])
print('Результат:', result)
