class BusDriver:
    def __init__(self, nm, sal, bNo):
        self.__name = nm
        self.__sal = sal
        self.__bNo = bNo

    # def display(self):
    #     print(f"Id={self.__bNo}\t Name={self.__name}\t sal={self.__sal}")

    def __str__(self):
        return f"Id={self.__bNo}\t Name={self.__name}\t sal={self.__sal}"


class ElectricBDriver(BusDriver):
    def __init__(self, nm, sal, bNo, exp):
        super().__init__(nm, sal, bNo)
        self.__exp = exp

    def __str__(self):
        return super().__str__() + f"\tExperience={self.__exp}"


busD = BusDriver("Sudhakar", 121222, 321)
ebd = ElectricBDriver("Vikas", 222222, "e34", 4)

a = 10

print(a)
print(busD)
print(ebd)

# busD.display()