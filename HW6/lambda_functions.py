# 1 Создать lambda функцию, которая принимает на вход
# имя и выводит его в формате “Hello, {name}”.

greeting = lambda name: f"Hello, {name}"


print(greeting("Yan"))


def mass_greeting(*names):
    """Создать lambda функцию, которая принимает на вход
    список имен и выводит их в формате “Hello, {name}” в
    другой список
        :param names: На вход подается список имен
        :return: Возвращается новый список имен с приветствием
    """
    return list(map(lambda name: f"Hello, {name}", names))


print(mass_greeting("Yan", "Greg", "Anna"))
