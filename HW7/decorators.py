def typed(type):
    def decorator(func):
        def wrapper(*args):
            converted_args = []
            for i, arg in enumerate(args):
                try:
                    converted_args.append(type(arg))
                except ValueError:
                    print(f"Аргумент {i+1} имеет неверный тип")
                    return None
            return func(*converted_args)

        return wrapper

    return decorator


@typed(type=str)
def add_two_symbols(a, b):
    return a + b


@typed(type=int)
def add_three_symbols(a, b, c):
    return a + b + c


print(add_two_symbols("dfsd", 5))

print(add_three_symbols(1, "dsfsdf", 3))
