def caesar_cipher_rus(text, shift):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ''
    for letter in text:
        if letter == ' ':
            encrypted_text += ' '
        else:
            ind = alphabet.index(letter.lower()) + shift
            if ind > 32:
                ind -= 33
            encrypted_text += alphabet[ind]
    return encrypted_text


in_file = open('text.txt', 'r', encoding='utf8')
out_file = open('cipher_text.txt', 'a', encoding='utf8')
line_number = 1
for line in in_file:
    line = line[:-1]
    caesar_line = caesar_cipher_rus(line, line_number)
    out_file.write(caesar_line + '\n')
    line_number += 1
in_file.close()
out_file.close()
