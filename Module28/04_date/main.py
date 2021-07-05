class Date:
    """
    Класс для работы с датой в строковом виде. Должен получать на вход строку вида ‘dd-mm-yyyy’.
    Методы проверяют числа даты на корректность, конвертируют строку даты в объект класса Date, состоящий из
     соответствующих числовых значений дня, месяца и года.
    """
    date_string = ''
    day = ''
    month = ''
    year = ''

    @classmethod
    def from_string(cls, date_string: str):
        cls.date_string = date_string
        cls.day = cls.date_string[:2]
        cls.month = cls.date_string[3:5]
        cls.year = cls.date_string[6:]
        return cls()

    @classmethod
    def is_date_valid(cls, data_string: str) -> bool:
        cls.from_string(data_string)
        if cls.day.isdigit() and cls.month.isdigit() and cls.year.isdigit():
            if 0 < int(cls.day) < 32 and 0 < int(cls.month) < 13:
                return True
        return False

    @classmethod
    def __str__(cls) -> str:
        return f'День: {cls.day} Месяц: {cls.month} Год: {cls.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# зачёт!
