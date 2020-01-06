class Flowers:

    def __init__(self,name,petals,price):
        self.name = name
        self.petals = int(petals)
        self.price = float(price)

    def get_name(self):
        return self.name

    def get_petals(self):
        return self.petals

    def get_price(self):
        return self.price