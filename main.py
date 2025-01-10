import random
import datetime


def isEven(value: int) -> bool:
    """ Функция определения четности целого числа. """
    _, b = str((value / 2)).split('.')
    if int(b) != 0:
        return False
    return True


class MyBof:
    """ Циклический буфер FIFO """
    def __init__(self, size):
        self.size: int = size
        self.cursor_bof = 0
        self.bof: dict = {}

        for s in range(size):
            self.bof[s] = None

    def __str__(self) -> str:
        return f'Bof {self.size}'

    def get_bof(self) -> dict:
        """ Получаем весь буфер """
        return self.bof

    def get_cursor_bof(self):
        """ Получаем следующую ячейку буфера для перезаписи """
        if self.cursor_bof > self.size:
            self.cursor_bof = 0
        return self.cursor_bof

    def get_iter_bof(self, start: int, n: int) -> list:
        """ Получаем интервал значение буфера """
        if start > self.size:
            raise Exception(f'Превышен порог адресации буфера. Размер буфера {self.size}')
        list_data: list = []
        for i in range(n):
            self.cursor_bof = start
            list_data.append(self.bof.get(start+i))
        return list_data

    def add_bof(self, data):
        """ Добавление элементов в буфер """
        cur = MyBof.get_cursor_bof(self)
        self.cursor_bof += 1
        self.bof[cur] = data
        return self.bof[cur]


def foo(data: list) -> list:
    """ Функция сортировки списка """
    sort_data = []
    if len(sort_data) == 0:
        sort_data.append(data[0])
    len_data = range(len(data))

    for i in data:
        for k in len_data:
            if i < sort_data[k]:
                sort_data.insert(k, i)
                break
            if sort_data[k] == sort_data[-1]:
                sort_data.append(i)
                break
    return sort_data


print("\nЗадание 1:")
n = 654065406541
n_2 = 65406540654
a = isEven(n)
a_2 = isEven(n_2)
print(n, a)
print(n_2, a_2)

print("\nЗадание 2:")
bof = MyBof(size=10)
# Проверяем размер буфера и наличие данных
print(bof)
print(bof.get_bof())
# Заполняем буфер
for i in range(55):
    bof.add_bof(i)
# Проверяем цикличность буфера
print(bof.get_bof())
# Получаем интервал значений буфера
print(bof.get_iter_bof(4, 5))

print("\nЗадание 3:")
data = []
for i in range(10000):
    data.append(random.randrange(1, 999, 1))
print(data)
time_start = datetime.datetime.now()
sort_data = foo(data)
time_end = datetime.datetime.now()
print(sort_data)
print(time_end - time_start)
