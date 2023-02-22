import struct
import random


def slice_nums(filename: str) -> (str, tuple):
    """Функция выводит первый, второй, предпоследний и последний
     элементы файла. Если чисел меньше 3 выводит ошибку.
    :param filename: На вход принимается файл в формате txt
    :return: функция возвращает строку и кортеж
    """
    try:
        with open(filename, "r") as f1:
            numbers = [int(num) for num in f1.read().split()]
            if len(numbers) < 4:
                return "Ошибка: в файле меньше 3-х чисел"
            else:
                return numbers[0], numbers[1], numbers[-2], numbers[-1]
    except FileNotFoundError:
        print("Файл не найден")


def separate_nums(filename):
    """Функция на вход принимает файл с целыми числами. Создает два новых
    файла, первый из которых содержит четные числа из исходного файла, а
    второй — нечетные (в том же порядке). Если четные или нечетные числа в
    исходном файле отсутствуют, то соответствующий результирующий файл
    оставить пустым.
    """
    even_num = []
    odd_num = []

    with open(filename, "r") as f:
        for line in f:
            num = int(line.strip())
            if num % 2 == 0:
                even_num.append(num)
            else:
                odd_num.append(num)
    if even_num:
        with open("even_nums.txt", "w") as f:
            for num in even_num:
                f.write(str(num) + "\n")
    if odd_num:
        with open("odd_nums.txt", "w") as f:
            for num in odd_num:
                f.write(str(num) + "\n")


def square_number(filename):
    """Функция заменяет все целые числа в файле на их квадраты."""
    try:
        with open(filename, "r") as f:
            numbers = f.read().split()
        numbers = [int(x) ** 2 for x in numbers]
        with open(filename, "w") as f:
            f.write("\n".join(map(str, numbers)))
    except FileNotFoundError:
        print("Файл не найден")


def create_two_bin_files():
    try:
        with open("file4.bin", "xb") as f1, open("file5.bin", "xb") as f2:
            for i in range(10):
                num = random.randint(0, 100)
                f1.write(struct.pack("i", num))
                num = random.randint(0, 100)
                f2.write(struct.pack("i", num))
    except FileExistsError:
        print("Ошибка: Файл уже существует")


def swap_files(file4, file5):
    # Функция меняет содержмое двух бинарных файлов между собой.
    try:
        # открываем два бинарных файла и читаем из них содержимое
        with open("file4.bin", "rb") as f1, open("file5.bin", "rb") as f2:
            data1 = f1.read()
            data2 = f2.read()

        # записываем содержимое первого файла во второй и наоборот
        with open("file4.bin", "wb") as f1, open("file5.bin", "wb") as f2:
            f1.write(data2)
            f2.write(data1)
    except FileNotFoundError:
        print("Ошибка: файл не найден")
