def func_2003(inp_tuple, element):
    if element not in inp_tuple:
        new_tuple = ()
    else:
        start_index = inp_tuple.index(element)
        if inp_tuple.count(element) == 1:
            new_tuple = inp_tuple[start_index:]
        else:
            end_index = start_index + 1 + inp_tuple[start_index + 1:].index(element)
            new_tuple = inp_tuple[start_index:end_index + 1]
    return new_tuple


input_tuple = ('1', '2', '3', '8', '3', '6', '8', '2', '3', '9')
input_element = input('Введите элемент: ')

out_tuple = func_2003(input_tuple, input_element)
print(out_tuple)

# зачёт!
