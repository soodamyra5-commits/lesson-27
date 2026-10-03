class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print(f"Selling Price: {self.__maxprice}")

    def setMaxPrice(self, price):
        self.__maxprice = price
obj_1 = Computer()
obj_1.sell()
obj_1.__maxprice = 1000
obj_1.sell()
print(obj_1.__maxprice)
obj_1.setMaxPrice(1500)
obj_1.sell()



