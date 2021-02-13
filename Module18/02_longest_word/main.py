text_list = input('Введите текст: ').split()
max_length = 0
longest_word = ''
for word in text_list:
    if len(word) > max_length:
        max_length = len(word)
        longest_word = word
print(f'Самое длинное слово "{longest_word}", его длина - {max_length} букв.')
