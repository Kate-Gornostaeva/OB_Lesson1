#Ты разрабатываешь программное обеспечение для сети магазинов.
#Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики,
#такие как адрес, название и ассортимент товаров.
#Ваша задача — создать класс `Store`, который можно будет использовать для создания различных магазинов.

class Store():
    items = {}
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

#Добавление товара в список
    def add_item (self):
        item_name = input("Введите наименование товара: ")
        item_price = int(input("Введите цену товара: "))
        Store.items[item_name] = item_price

#Удаление товара из списка
    def remove_item(self):
        item_name = input("Введите наименование товара для удаления из списка: ")
        if item_name in Store.items:
            del Store.items [item_name]
        else:
            print("Данный товар отсутствует в списке")
            None

#Получение цены товара по названию
    def price_info(self):
        item_name = input("Введите наименование товара, цену которого хотите узнать: ")
        item_price = Store.items [item_name]

#Обновление цены товара
    def new_price (self):
        item_name = input("Введите наименование товара для изменения цены: ")
        new_item_price = int(input("Введите новую цену товара: "))
        Store.items [item_name] = new_item_price

store_1 = Store("Саквояжик","улица Фруктовая, 5")
store_2 = Store("Сумка", "улица Садовая, 54")
store_3 = Store("Авоська", "улица Огородная, 18")




