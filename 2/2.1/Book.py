class Book:
    def __init__(self, author, title, price):
        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def get_author(self):
        return self.__author

