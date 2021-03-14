site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(struct, key, depth):
    if depth > 0:
        if key in struct:
            return struct[key]
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


user_key = input('Какой ключ ищем? ')
search_depth = int(input('Задайте глубину поиска (0 - без ограничений): '))
if search_depth < 1:
    search_depth = 1000
value = find_key(site, user_key, search_depth)
if value:
    print(value)
else:
    print('Нет такого ключа')

# зачёт!
