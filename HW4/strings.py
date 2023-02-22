""" 1. Свяжите переменную с любой строкой, состоящей не менее чем из
8 символов. Извлеките из строки первый символ, затем последний,
третий с начала и третий с конца. Измерьте длину вашей строки.
"""


def changing_string(string):
    lst_rand_str1 = list(string)
    lst_rand_str1.pop(0)
    lst_rand_str1.pop(8)
    lst_rand_str1.pop(2)
    lst_rand_str1.pop(-3)
    new_rand_str1 = "".join(lst_rand_str1)
    return new_rand_str1, len(new_rand_str1)


# 2. Присвойте произвольную строку длиной 10-15 символов переменной
# и извлеките изнее следующие срезы.
def slices_from_string(rand_str2):
    """первые восемь символов
    четыре символа из центра строки
    символы с индексами кратными трем
    переверните строку
    """

    slc1_rand_str2 = rand_str2[:8]
    print(slc1_rand_str2)
    slc2_rand_str2 = rand_str2[5:-5]
    print(slc2_rand_str2)

    for i in range(len(rand_str2)):
        if i % 3 == 0:
            print(rand_str2[i])
    slc4_rand_str2 = rand_str2[::-1]
    print(slc4_rand_str2)


# 3. Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name”
# вставьте ваше имя.
def change_name(string, name):
    spl_name = string.split()
    spl_name[3] = name
    return " ".join(spl_name)


# 4. Есть строка: test_string = "Hello world!", необходимо
# ● напечатать на каком месте находится буква w
# ● кол-во букв l
# ● Проверить начинается ли строка с подстроки: “Hello”
# ● Проверить заканчивается ли строка подстрокой: “qwe”
def actions_string(test_string):
    print(test_string.index("w"))
    count = 0
    for i in test_string:
        if i == "l":
            count += 1
    print(count)
    print(test_string.startswith("Hello"))
    print(test_string.endswith("qwe"))
