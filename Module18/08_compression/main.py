data = input('Введите строку: ')
i_symbol = 0
compressed_data = []
while i_symbol < len(data):
    compressed_data.append(data[i_symbol])
    symbol_count = 1
    while i_symbol < len(data) - 1 and data[i_symbol] == data[i_symbol + 1]:
        symbol_count += 1
        i_symbol += 1
    compressed_data.append(str(symbol_count))
    i_symbol += 1
compressed = ''.join(compressed_data)
print('Закодированная строка: ', compressed)

# зачёт!
