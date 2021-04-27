class MyDict(dict):
    def get(self, key):
        if key in self:
            return self[key]
        else:
            return 0


dict_1 = {'0': '00', '1': '11', '2': '22'}

print(dict_1.get('1'))
print(dict_1.get('4'))

dict_2 = MyDict()
dict_2['0'] = '000'
dict_2['1'] = '111'

print(dict_2.get('1'))
print(dict_2.get('4'))

#  не понимаю, как исправить метод get, что-бы по умолчанию возвращать не None, а число 0.
# Как я понимаю, класс class MyDict(dict)  нужно наследовать от класса dict, в котором есть метод  get, который и надо
# переопределить. Но я вижу только такой код

# class dict(object):
#     def get(self, *args, **kwargs): # real signature unknown
#         """ Return the value for key if key is in the dictionary, else default. """
#         pass
# где найти код метода get, который нужно переопределить? Или другое решение должно-быть?

#  вариант с MyDict(dict) правильный и в этом классе необходимо описать метод get.
#  Сам объект dict менять при это не нужно.

# зачёт!
