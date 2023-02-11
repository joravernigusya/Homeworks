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
school = {
    "1a": 18,
    "2б": 30,
    "3в": 21,
    "4г": 25,
    "5д": 19,
    "6у": 27,
    "7ж": 30,
    "8з": 22,
    "9и": 24,
    "10к": 26,
}
print(school.get("5д"))
school["1a"] = 19
school["2б"] = 29
school["3в"] = 25
school["11л"] = 15
school["12м"] = 42
school["13н"] = 56
del school["4г"]
print(school)
