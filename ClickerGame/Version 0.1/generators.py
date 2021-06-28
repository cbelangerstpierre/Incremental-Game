class Generators:
    def __init__(self, boost, price):
        self.boost = boost
        self.price = price
        self.number_owned = 0

    def setBoost(self, boost):
        self.boost = boost

    def setPrice(self, price):
        self.price = price

    def setNumberOwned(self, number_owned):
        self.number_owned = number_owned

    def getBoost(self):
        return self.boost

    def getPrice(self):
        return self.price

    def getNumberOwned(self):
        return self.number_owned


first_generator = Generators(1, 10)
second_generator = Generators(10, 200)
third_generator = Generators(100, 3000)
