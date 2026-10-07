class BusDriver:
    def __init__(self, depoName, driverName, busNo):
        self.depoName = depoName
        self._driverName = driverName
        self.__busNo = busNo

    def display(self):
        print(f"Depo Name : {self.depoName}")
        print(f"Driver Name : {self._driverName}")
        print(f"Bus No : {self.__busNo}")

b = BusDriver("Kolhapur", "Amit", "MH09 CD 5678")
b.display()

print("\nAccessing Members:")
print("Depo Name :", b.depoName)
print("Driver Name :", b._driverName)