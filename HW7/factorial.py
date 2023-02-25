import timeit


# Написать обычную функцию для факториала, генератор и
# рекурсию. Сравнить их время работы.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_generator(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        yield result


def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n - 1)


n = 10

print(f"Время выполнения простой функции факториала: ",
      timeit.timeit(lambda: factorial(n), number=100000))
print("Время выполнения генератора факториала: ",
      timeit.timeit(lambda: list(factorial_generator(n)), number=100000))
print("Время выполнения рекурсии факториала: ",
      timeit.timeit(lambda: factorial_recursion(n), number=100000))
