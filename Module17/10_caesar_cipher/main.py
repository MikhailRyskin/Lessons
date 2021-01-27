# alphabet = [а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я]
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите сообщение: ')
k = int(input('Введите сдвиг: '))
encrypted_text = ''
for letter in text:
    if letter == ' ':
        encrypted_text += ' '
    else:
        ind = alphabet.index(letter) + k
        if ind > 32:
            ind -= 33
        encrypted_text += alphabet[ind]
print('Зашифрованное сообщение:', encrypted_text)

# зачёт!
