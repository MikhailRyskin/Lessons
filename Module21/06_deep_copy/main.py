# from pprint import pprint


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def insert_model(struct, model):
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            if 'title' in sub_struct.keys():
                sub_struct['title'] = f'Куплю/продам {model} недорого'
            elif 'h2' in sub_struct.keys():
                sub_struct['h2'] = f'У нас самая низкая цена на {model}'
                break
            insert_model(sub_struct, model)


site_counter = int(input('Сколько сайтов: '))
for _ in range(site_counter):
    product = input('\nВведите название продукта для нового сайта: ')
    print(f'\nСайт для {product}: ')
    insert_model(site, product)
    print(site)
    # pprint(site)
