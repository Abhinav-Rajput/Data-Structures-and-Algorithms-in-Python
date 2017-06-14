# Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its number
# of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type


class Flower:
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    def set_name(self, name):
        self.name = name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price

    def get_name(self,):
        return self.name

    def get_petals(self,):
        return self.petals

    def get_price(self,):
        return self.price

    def displayAll(self,):
        print("name: {0}, petals: {1}, and price: {2} ".format(
            self.name, self.petals, self.price))


if __name__ == '__main__':
    print('Initial Values')
    obj = Flower('rose', 10, 20)
    obj.displayAll()
    print("set name = gardenia")
    obj.set_name('gardenia')
    print(obj.get_name())
    print("set_price = 5")
    obj.set_price(5)
    print(obj.get_price())
    print("set petals = 1")
    obj.set_petals(1)
    print(obj.get_petals())
    print('NEW Values')
    obj.displayAll()
