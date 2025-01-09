import random
import datetime

from src import isEven, MyBof, foo


def main():

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


if __name__ == "__main__":
    main()
