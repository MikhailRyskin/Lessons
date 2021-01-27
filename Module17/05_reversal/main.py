text = input('Введите строку( h минимум 2 раза): ')
start_ind = 0
finish_ind = 0
first = True
for ind in range(len(text)):
    if text[ind] == 'h':
        if first:
            start_ind = ind
            first = False
        else:
            finish_ind = ind
print(text[finish_ind - 1:start_ind:-1])
