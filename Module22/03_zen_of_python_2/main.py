from collections import defaultdict


file = open('zen.txt', 'r')
number_lines = 0
number_words = 0
letters = defaultdict(int)
for line in file:
    number_lines += 1
    number_words += len(line.split())
    for symbol in line:
        if symbol.isalpha():
            letters[symbol.lower()] += 1
number_letters = 0
min_letter = ''
min_count = number_words
for letter, count in letters.items():
    number_letters += count
    if count < min_count:
        min_letter = letter
        min_count = count
file.close()

print('Число строк', number_lines)
print('Число слов', number_words)
print('Число букв', number_letters)
print(f'Наименьшее количество раз - {min_count} встречается буква {min_letter}.')
