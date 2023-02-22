""" 1. Создайте словарь, связав его с переменной school, и наполните
 его данными, которые бы отражали количество учащихся в десяти разных
 классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
2. Узнайте сколько человек в каком-нибудь классе.
3. Представьте, что в школе произошли изменения, внесите их в словарь:
◦ в трех классах изменилось количество учащихся;
◦ в школе появилось два новых класса;
◦ в школе расформировали один из классов.
4. Выведите содержимое словаря на экран.
"""


def school_changes():
    school = {
        "1a": 20,
        "2b": 22,
        "3c": 18,
        "4d": 24,
        "5e": 16,
        "6f": 20,
        "7g": 25,
        "8h": 21,
        "9i": 19,
        "10j": 23,
    }

    # Выводим количество учеников в классе 3d
    print("Количество учеников в классе 10j:", school["10j"])

    # Изменяем количество учащихся в трех классах
    school["1a"] = 18
    school["5e"] = 22
    school["9i"] = 21

    # Добавляем два новых класса и удаляем один класс
    school["11k"] = 17
    school["12l"] = 19
    del school["7g"]

    # Выводим содержимое словаря
    for k, v in school.items():
        print(k, ":", v)
