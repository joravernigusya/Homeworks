"""1. Даны два целых числа A и B (A < B). Найти сумму всех целых чисел
 от A до B включительно.
"""


def sum_of_numbers(a, b):
    sum = 0
    for i in range(a, b + 1):
        if a < b:
            sum += i
    return sum


# 2. Найти сумму всех натуральных чисел в от A до B.
def sum_of_numbers2(a, b):
    print(sum(range(a, b)))


# 3. Найти произведение положительных, сумму и количество отрицательных
# из 10 введенных целых значений.
def mult_sum_count_num(*args):
    mult_pos_num = 1
    count_neg_num = 0
    sum_neg_num = 0
    for i in args:
        if i > 0:
            mult_pos_num *= i
        elif i < 0:
            count_neg_num += 1
            sum_neg_num += i
    return mult_pos_num, sum_neg_num, count_neg_num


# 4. Дан словарь пловцов с их результатами. Напечатать лучший результат
# заплыва среди 6 участников.
# Бекиш Александр - 21,07
# Будник Алексей - 20,34
# Гребень Анастасия - 22,12
# Давидович Татьяна - 30
# Дешук Дмитрий - 24.01
# Казак Анна - 28,17
def best_swimmer(swimmers):
    max_value = max(swimmers.values())
    max_score = {k: v for k, v in swimmers.items() if v == max_value}
    return max_score


# 5. Есть массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5. Напишите программу,
# которая будет выводить уникальное число.
def list_uniq_num(*args):
    for i in args:
        if args.count(i) == 1:
            return i
