""" 1. Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" =>
["I", "love", "arrays", "they", "are", "my", "favorite"]
"""
string1 = "Robin Singh"
lst_string1 = string1.split()
string2 = "I love arrays they are my favorite"
lst_string2 = string2.split()
print(lst_string1, lst_string2, sep="\n")

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

lst_name = ["Ivan", "Ivanou"]
republic = "Belarus"
city = "Minsk"
print(f"Привет, {' '.join(lst_name)}! Добро пожаловать в {city} {republic}")

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite".

string3 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(string3))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6.

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst1[3] = 99
lst1.pop(6)
print(lst1)

# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить
# в список, если у одного словаря есть ключ "а", а у другого нету,
# то поставить значение None на соответствующую позицию(1-я позиция
# для 1-ого словаря, вторая для 2-ого) ab = {'a': [1, None],
# 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}.

a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
joined_a_b = {
    key: [a.get(key, None), b.get(key, None)] for key in sorted(set(a) | set(b))
}
print(joined_a_b)
