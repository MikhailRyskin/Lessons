while True:
    parole = input('Придумайте пароль: ')
    capital_letter = False
    num_digits = 0
    for letter in parole:
        if letter.isupper():
            capital_letter = True
        if letter.isdigit():
            num_digits += 1
    if len(parole) < 8 or num_digits < 3 or not capital_letter:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
        break
