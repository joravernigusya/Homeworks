import random

# 1. Создайте два любых списка и свяжите их с переменными.
# 2. Извлеките из первого списка второй элемент.
# 3. Измените во втором списке последний элемент. Выведите список
# на экран.
# 4. Соедините оба списка в один, присвоив результат новой переменной.
# Выведите получившийся список на экран.
# 5. "Снимите" срез из соединенного списка так, чтобы туда попали
# некоторые части обоих первых списков. Срез свяжите с очередной
# новой переменной. Выведите значение этой переменной.
# 6. Добавьте в список два новых элемента и снова выведите его.


def two_lists(list1, list2):
    list1.remove(2)
    list2[-1] = random.randrange(0, 100)
    print(list2)
    join_list1_list2 = list1 + list2
    print(join_list1_list2)
    slice_list1_list2 = join_list1_list2[1:-1]
    print(slice_list1_list2)
    add_char = ["cow", "goat"]
    slice_list1_list2 += add_char
    print(slice_list1_list2)


# 7. Даны списки:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13].
# Нужно вернуть список, который состоит из элементов,
# общих для этих двух списков.


def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_elem = list(set1.intersection(set2))
    return common_elem


# 8. Есть список: [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
# оставить в нем только уникальные значения. !не использовать циклы.


def uniq_elem_list(list):
    uniq_list = set(list)
    return uniq_list
