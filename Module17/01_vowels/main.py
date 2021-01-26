vowels = 'ауоыиэяюёе'
text = input('Введите текст: ')
vowels_list = [letter for letter in text if vowels.find(letter) != -1]
print('Список гласных букв:', vowels_list)
print('Длина списка:', len(vowels_list))
