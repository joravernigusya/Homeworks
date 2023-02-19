""" 1. Присвойте двум переменным любые числовые значения.
2. Составьте четыре сложных логических выражения с помощью
оператора and, два из которых должны давать истину, а два других - ложь.
3. Аналогично выполните п. 2, но уже используя оператор or.
4. Попробуйте использовать в сложных логических выражениях
работу с переменными строкового типа.
"""


def logical_operation(a, b, str1, str2):
    print(a < b and b >= 15)
    print(a == 10 and b != 100)
    print(a > b and b < a)
    print(a == b and b <= 0)
    print(a < b or b <= 15)
    print(a == 10 or b == 100)
    print(a == 20 or b != 20)
    print(a < 10 or b > 20)
    print(str1 != str2 and str1 < str2)
    print(str1 < str2 and str2 == str1)
    print(str1 > str2 or str2 != str1)
    print(str1 == 0 or str2 == 0)
