text_list = input('Введите строку: ').split()  # TODO, вместо split можно сразу использовать title =)
result = ' '.join([word.title() for word in text_list])
print('Результат:', result)

