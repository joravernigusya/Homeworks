# 1. Привести к целому типу -1.6, 2.99.
first_num = int(-1.6)
second_num = int(2.99)
print(first_num)
print(second_num)

"""2. Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'. 
Решение представлено двумя сопособами.

"""
url_string = "www.my_site.com#about"
list_url_string = list(url_string)
list_url_string[-6] = "/"
url_string = ''.join(list_url_string)
print(url_string)

url_string = "www.my_site.com#about"
updated_url_string = url_string.replace("#", "/")
print(updated_url_string)

"""3. Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’.
Решение представлено тремя способами.

"""
first_str = "sing"
second_str = "ing"
print(f"I like {first_str}{second_str}")
print("I like {word1}{word2}".format(word1=first_str, word2=second_str))
print("I like " + first_str + second_str)

# 4. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou".
name = "Ivanou Ivan"
updated_name = " ".join(name.split()[::-1])
print(updated_name)

""" 5. Напишите программу которая удаляет пробел в начале, в конце строки.
Задача представлена двумя способами.

"""
str1 = " Cъешь ещё этих мягких французских булок, да выпей чаю "
list_str1 = list(str1)
list_str1[0] = ""
list_str1[-1] = ""
print("".join(list_str1))

str2 = " Cъешь ещё этих мягких французских булок, да выпей чаю "
fixed_str2 = " ".join(str2.split())
print(fixed_str2)

""" 6. Создайте словарь, связав его с переменной school, и наполните его 
данными, которые бы отражали количество учащихся в десяти разных классах
(например, 1а, 1б, 2б, 6а, 7в и т.д.).

"""
school = {'1a': 18, '2б': 30, '3в': 21, '4г': 25, '5д': 19, '6у': 27, '7ж': 30, '8з': 22, '9и': 24, '10к': 26}

# 7. Создайте список и извлеките из него списка второй элемент.
num_list = [1, 2, 3, 4, 5, 6, 7]
print(num_list.pop(1))
print(num_list[1])  # - второй с начала
print(num_list[-2])  # - второй с конца

# 8. Вывести входит ли строка1 в строку2 (пример: employ и employment).
str1 = "employ"
str2 = "employment"
print(str1 in str2)

""" 9. Вывести нужные символы
x = "My name is Agent Smith"
print(x[?]) #y
print(x[?:?:?]) #nesgt

"""
x = "My name is Agent Smith"
print(x[1])
print(x[3:16:3])

# Задание 1.3 лекции.
x = ((17 / 2) * 3) + 2
print(x)
x = 2 + ((17 / 2) * 3)
print(x)
x = (19 % 4) + ((15 / 2) * 3)
print(x)
x = (15 + 6) - (10 * 4)
print(x)
x = ((17 / 2) % 2) * (3 ** 3)
print(x)

# Задание 1.4 лекции.
ivan_age = 40
lisa_age = 29
vera_age = 20
print(ivan_age + lisa_age + vera_age)
print(int((ivan_age + lisa_age + vera_age) / 3))