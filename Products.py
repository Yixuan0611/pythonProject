class Products:
    count_id = 0

    def __init__(self, name, price, quantity, description):
        Products.count_id += 1
        self.__product_id = Products.count_id
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__description = description

    # Getter methods

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity

    def get_description(self):
        return self.__description

    # Setter methods

    def set_product_id(self, product_id):
        self.__product_id = product_id

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_description(self, description):
        self.__description = description
