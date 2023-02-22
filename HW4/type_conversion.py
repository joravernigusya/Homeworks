# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
def string_to_array(str1, str2):
    lst_str1 = str1.split()
    lst_str2 = str2.split()
    return lst_str1, lst_str2


# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
def greeting(list, republic, city):
    print(f"Привет, {' '.join(list)}! Добро пожаловать в {city} {republic}")


# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite".
def list_to_string(list):
    converted_string = " ".join(list)
    return converted_string


# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое
# значение, удалите элемент из списка под индексом 6.
def changing_list(list):
    list[3] = 99
    list.pop(6)
    return list


# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
# Необходимо их объединить по ключам, а значения ключей поместить
# в список, если у одного словаря есть ключ "а", а у другого нету,
# то поставить значение None на соответствующую позицию(1-я позиция
# для 1-ого словаря, вторая для 2-ого) ab = {'a': [1, None],
# 'b': [2, None], 'c': [3, 3], 'd': [None, 4], 'e': [None, 5]}.
def join_dict(dict1, dict2):
    joined_dict = {
        key: [dict1.get(key, None), dict2.get(key, None)]
        for key in sorted(set(dict1) | set(dict2))
    }
    return joined_dict
