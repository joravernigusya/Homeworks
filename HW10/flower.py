class Flower:
    """Создание класса Цветок с методом времени увядания"""

    def __init__(self, name, freshness, length, color, price):
        self.name = name
        self.freshness = freshness
        self.length = length
        self.color = color
        self.price = price

    def get_wilt_time(self):
        if self.name == "Роза":
            return 5
        elif self.name == "Тюльпан":
            return 3
        elif self.name == "Гвоздика":
            return 4
        else:
            return 0

    def __str__(self):
        return f"{self.name} ({self.color}, {self.length} см., " \
               f"{self.price} руб.)"


class Accessory:
    """Создание класса Аксессуар с параметрами имени и цены"""

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} руб)"


class Bouquet:
    """Создание класса Букет с методами по добавлению цветка в букет,
    добавлению к цветку аксессуара, получению стоимости букета, вычислению
    времени увядания, сортировки по цене и нахождению цветка в букете"""

    def __init__(self):
        self.flowers = []
        self.accessories = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_accessory(self, accessory):
        self.accessories.append(accessory)

    def get_cost(self):
        return sum(flower.price for flower in self.flowers) + sum(
            accessory.price for accessory in self.accessories
        )

    def get_wilt_time(self):
        return sum([flower.get_wilt_time() for flower in self.flowers]) / len(
            self.flowers
        )

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def has_flower(self, flower):
        return flower in self.flowers


# Создаем несколько цветов
rose = Flower("Роза", 5, 50, "Красный", 100)
tulip = Flower("Тюльпан", 3, 30, "Желтый", 50)
carnation = Flower("Гвоздика", 4, 40, "Розовый", 70)

# Создаем несколько аксессуаров
ribbon = Accessory("Лента", 20)
wrapper = Accessory("Обертка", 30)

# Создаем букет и добавляем в него цветы и аксессуары
bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(carnation)
bouquet.add_accessory(ribbon)
bouquet.add_accessory(wrapper)

# Вычисляем стоимость букета
print("Стоимость букета:", bouquet.get_cost())

# Вычисляем время увядания букета
print("Время увядания букета:", bouquet.get_wilt_time())

# Сортируем цветы в букете по стоимости
bouquet.sort_by_price()
print("Цветы в букете, отсортированные по стоимости:")
for flower in bouquet.flowers:
    print(flower)

# Проверяем, есть ли цветок в букете
print("Цветок 'Роза' в букете:", bouquet.has_flower(rose))
print("Цветок 'Хризантема' в букете:", bouquet.has_flower(Flower))
