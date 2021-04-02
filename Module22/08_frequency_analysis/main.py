from collections import defaultdict


text_file = open('text.txt', 'r', encoding='utf8')
letters_stat = defaultdict(int)
total_letters = 0
for line in text_file:
    for symbol in line[:-1]:
        if symbol.isalpha():
            letters_stat[symbol.lower()] += 1
            total_letters += 1
for letter in letters_stat:
    letters_stat[letter] = round(letters_stat[letter] / total_letters, 3)

quantity_stat = {}
for letter, quantity in letters_stat.items():
    if quantity in quantity_stat:
        quantity_stat[quantity].append(letter)
    else:
        quantity_stat[quantity] = [letter]

analysis_file = open('analysis.txt', 'w', encoding='utf8')
for quantity in sorted(quantity_stat.keys(), reverse=True):
    for letter in sorted(quantity_stat[quantity]):
        analysis_file.write(f'{letter}  {quantity}\n')

text_file.close()
analysis_file.close()
