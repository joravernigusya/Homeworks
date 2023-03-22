# 1. Привести к целому типу -1.6, 2.99.
def convert_to_int(a, b):
    return int(a), int(b)


# 2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'.
def replace_char(string_with_char):
    return string_with_char.replace("#", "/")


# 3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’.
def gerund(string):
    print(string + "ing")


# 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
def update_name(name):
    print(" ".join(name.split()[::-1]))


# 5. Напишите программу которая удаляет пробел в начале, в конце строки.
# Задача представлена двумя способами.
# Чек-лист:
# 1) Проверить, что функция удаляет все пробелы в начале строки.
# 2) Проверить, что функция удаляет все пробелы в конце строки.
# 3) Проверить, что функция удаляет все пробелы, если они находятся и
# в начале, и в конце строки.
# 4) Проверить, что функция не удаляет пробелы, которые находятся внутри строки
# 5) Проверить, что функция правильно обрабатывает строки с одним пробелом
# или без пробелов.
def strip_string(string):
    print(string.strip())


# 6. Создайте словарь, связав его с переменной school, и наполните его
# данными, которые бы отражали количество учащихся в десяти разных классах
# (например, 1а, 1б, 2б, 6а, 7в и т.д.).
def dict_school(name, **obj):
    print(name, obj)


# 7. Создайте список и извлеките из него второй элемент.
def pop_num_list(list):
    print(list.pop(1))
    print(list)


# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment).
def str1_in_str2(string1, string2):
    print(string1 in string2)


# 9. Вывести нужные символы
# x = "My name is Agent Smith"
# print(x[?]) #y
# print(x[?:?:?]) #nesgt
def print_char(string):
    return string[1], string[3:16:3]


# Задание 1.3 лекции.
# x = ((17 / 2) * 3) + 2
# print(x)
# x = 2 + ((17 / 2) * 3)
# print(x)
# x = (19 % 4) + ((15 / 2) * 3)
# print(x)
# x = (15 + 6) - (10 * 4)
# print(x)
# x = ((17 / 2) % 2) * (3 ** 3)
# print(x)
def calculation1():
    print(((17 / 2) * 3) + 2)
    print(2 + ((17 / 2) * 3))
    print((19 % 4) + ((15 / 2) * 3))
    print((15 + 6) - (10 * 4))
    print(((17 / 2) % 2) * (3**3))


# Задание 1.4 лекции.
# ivan_age = 40
# lisa_age = 29
# vera_age = 20
# print(ivan_age + lisa_age + vera_age)
# print(int((ivan_age + lisa_age + vera_age) / 3))
def calculation_ages(ivan_age, lisa_age, vera_age):
    print(ivan_age + lisa_age + vera_age)
    print(int((ivan_age + lisa_age + vera_age) / 3))
