import os


class File:
    """
    Контекст-менеджер. Обеспечивает обработку файла по названию и режиму.
    При попытке открыть несуществующий файл, создаёт и открывает этот файл в режиме записи.
    Подавляются все исключения, связанные с файлами.
    """

    def __init__(self, name: str, mode: str) -> None:
        self.name = name
        self.mode = mode
        self.file = None

    def __enter__(self):
        if os.path.exists(self.name) and os.path.isfile(self.name):
            self.file = open(self.name, self.mode, encoding='UTF-8')
        else:
            self.file = open(self.name, 'w', encoding='UTF-8')
            print(f'создан новый файл {self.name} в режиме записи')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            exc_str = exc_type.__name__.lower()
            if exc_str.find('file') != -1:
                print('было исключение', exc_type.__name__)
                return True


with File('example1.txt', 'a') as file:
    file.write('Всем привет!\n')
    # raise TypeError
    # raise FileNotFoundError

# зачёт!
