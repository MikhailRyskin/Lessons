number_pairs = int(input('Введите количество пар слов: '))
couples_list = []
#  Если переменную цикла используем в коде, её необходимо назвать так, чтобы название отражало суть содержания.
#  "i", "n" не отражают =)
#   исправил названия переменных
for i_pairs in range(1, number_pairs + 1):
    couple_words = input(f'{i_pairs} пара: ').title().split(' - ')
    couples_list.append(couple_words)
synonyms_dict1 = {couple[0]: couple[1] for couple in couples_list}
synonyms_dict2 = {couple[1]: couple[0] for couple in couples_list}
while True:
    word = input('Введите слово: ').title()
    if synonyms_dict1.get(word):
        print('Синоним:', synonyms_dict1[word])
        break
    elif synonyms_dict2.get(word):
        print('Синоним:', synonyms_dict2[word])
        break
    else:
        print('Такого слова в словаре нет.')

# зачёт!
