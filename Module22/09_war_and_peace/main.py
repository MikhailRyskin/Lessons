from collections import defaultdict
import zipfile


file_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
file_zip.extractall()
file = open('voyna-i-mir.txt', 'r', encoding='utf8')

letters_stat = defaultdict(int)
total_letters = 0
for line in file:
    for letter in line:
        if letter.isalpha():
            total_letters += 1
            letters_stat[letter] += 1

quantity_stat = {}
for letter, quantity in letters_stat.items():
    if quantity in quantity_stat:
        quantity_stat[quantity].append(letter)
    else:
        quantity_stat[quantity] = [letter]

print('Всего букв:', total_letters)
for quantity in sorted(quantity_stat.keys(), reverse=True):
    for letter in quantity_stat[quantity]:
        print(f'{letter}  {quantity} ')

file.close()
file_zip.close()
