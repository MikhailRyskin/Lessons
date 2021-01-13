word = input('Введите слово: ')
word_list = list(word)
unique_letters = 0

while len(word_list) != 0:
    new_word = []
    unique_flag = True
    first_letter = word_list[0]
    # TODO, или можем просто идти в цикле по word_list? =)
    #  Это позволило бы сократить количество срезов.
    for i in range(1, len(word_list)):
        if word_list[i] != first_letter:
            new_word.append(word_list[i])
        else:
            unique_flag = False
    if unique_flag:
        unique_letters += 1
    word_list = new_word
print('Кол-во уникальных букв:', unique_letters)

# TODO,
#  Введите слово: карамба
#  Кол-во уникальных букв: 4
#  По идее 5 =) к а р м б