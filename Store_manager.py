#Ты разрабатываешь программное обеспечение для сети магазинов.
#Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
#такие как адрес, название и ассортимент товаров.
#Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.

class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

#Добавление товара в список
    def add_item (self):
        item_name = input("Введите наименование товара: ")
        item_price = float(input("Введите цену товара: "))
        if item_price > 0:
            self.items[item_name] = item_price
            print(f"Товар {item_name} по цене {item_price} добавлен\n")
        else:
            print("Некорректный ввод цены")

#Удаление товара из списка
    def remove_item(self):
        item_name = input("Введите наименование товара для удаления из списка: ")
        if item_name in self.items:
            del self.items [item_name]
            print(f"Товар {item_name} удален\n")
        else:
            print("Данный товар отсутствует в списке")


#Получение цены товара по названию
    def price_info(self):
        item_name = input("Введите наименование товара, цену которого хотите узнать: ")
        try:
            item_price = self.items [item_name]
            print(f"Цена товара {item_name}: {item_price}\n")
        except KeyError:
            print("Товар не найден.")

#Обновление цены товара
    def new_price (self):
        item_name = input("Введите наименование товара для изменения цены: ")
        if item_name in self.items:
            new_item_price = float(input("Введите новую цену товара: "))
            self.items [item_name] = new_item_price
            print(f"Товар {item_name} по новой цене {new_item_price}\n")
        else:
            print("Данный товар отсутствует в списке")



store_1 = Store("Саквояжик","улица Фруктовая, 5")
store_2 = Store("Сумка", "улица Садовая, 54")
store_3 = Store("Авоська", "улица Огородная, 18")

while True:
    user_choice_store = int(input(f"\nВыберите магазин, со списком товаров которого вы хотите работать:"
                              f"\n 1: {store_1.name}, {store_1.address}"
                              f"\n 2: {store_2.name}, {store_2.address}"
                              f"\n 3: {store_3.name}, {store_3.address}\n: "))
    if user_choice_store == 1:
        task = int(input("\n Выберите дальнейшее действие:"
                         "\n Добавить товар к списку - 1"
                         "\n Удалить товар из списка - 2"
                         "\n Узнать цену определенного товара - 3"
                         "\n Обновить цену определенного товара - 4"
                         "\n Вывести список товаров - 5"
                         "\n Закончить работу со списками - 6\n :"))
        if task == 1:
            store_1.add_item()  # Добавить товар в первый магазин
        elif task == 2:
            store_1.remove_item()
        elif task == 3:
            store_1.price_info()
        elif task == 4:
            store_1.new_price()
        elif task == 5:
            print(store_1.items)
        else:
            break

    if user_choice_store == 2:
        task = int(input("\n Выберите дальнейшее действие:"
                          "\n Добавить товар к списку - 1"
                          "\n Удалить товар из списка - 2"
                          "\n Узнать цену определенного товара - 3"
                          "\n Обновить цену определенного товара - 4"
                          "\n Вывести список товаров - 5"
                         "\n Закончить работу со списками - 6\n :"))
        if task == 1:
            store_2.add_item()  # Добавить товар в первый магазин
        elif task == 2:
            store_2.remove_item()
        elif task == 3:
            store_2.price_info()
        elif task == 4:
            store_2.new_price()
        elif task == 5:
            print (store_2.items)
        else:
            break

    if user_choice_store == 3:
        task = int(input("\n Выберите дальнейшее действие:"
                          "\n Добавить товар к списку - 1"
                          "\n Удалить товар из списка - 2"
                          "\n Узнать цену определенного товара - 3"
                          "\n Обновить цену определенного товара - 4"
                          "\n Вывести список товаров - 5"
                         "\n Закончить работу со списками - 6\n :"))
        if task == 1:
            store_3.add_item()  # Добавить товар в первый магазин
        elif task == 2:
            store_3.remove_item()
        elif task == 3:
            store_3.price_info()
        elif task == 4:
            store_3.new_price()
        elif task == 5:
            print (store_3.items)
        else:
            break






