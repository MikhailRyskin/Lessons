def hist(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


text = input('Введите текст: ')
hist_dict = hist(text)
print('Оригинальный словарь частот:')
for i_sym in sorted(hist_dict.keys()):
    print(i_sym, ':', hist_dict[i_sym])
invert_dict = {hist_dict[letter]: [] for letter in hist_dict}
for sym in hist_dict:
    invert_dict[hist_dict[sym]].append(sym)
print('Инвертированный словарь частот:')
for quantity in sorted(invert_dict.keys()):
    print(quantity, ':', invert_dict[quantity])
