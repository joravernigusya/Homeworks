def slice_nums(filename):
    """Функция выводит первый, второй, предпоследний и последний
    элементы файла. Если чисел меньше 3 выводит ошибку.
    """
    try:
        with open(filename, "r") as f1:
            numbers = [int(num) for num in f1.read().split()]
            if len(numbers) < 4:
                print("Ошибка: в файле меньше 3-х чисел")
            else:
                print(numbers[0], numbers[1], numbers[-2], numbers[-1])
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


def swap_files(file4, file5):
    """Функция меняет содержмое двух бинарных файлов между собой."""
    try:
        with open(file4, "rb") as f4, open(file5, "rb") as f5:
            file4_data = f4.read()
            file5_data = f5.read()

        with open(file4, "wb") as f4, open(file5, "wb") as f5:
            f4.write(file5_data)
            f5.write(file4_data)
    except FileNotFoundError:
        print("Ошибка: файл не найден")
