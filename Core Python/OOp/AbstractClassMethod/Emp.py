from abc import ABC, abstractmethod

class Emp(ABC):
    def __init__(self, id, name, sal):
        self.__id = id
        self.__name = name
        self.__sal = sal

    @abstractmethod
    def calSal(self):
        pass

    def getId(self):
        return self.__id
    def setId(self, id):
        self.__id = id
    def getName(self):
        return self.__name
    def setName(self, nm):
        self.__name = nm
    def getSal(self):
        return self.__sal
    def setSal(self, sal):
        self.__sal = sal

    def display(self):
        print(f'Id={self.__id}\t name={self.__name}\t sal={self.__sal}')

# Hr class
class Hr(Emp):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.__com = com

    def calSal(self):
        final_sal = self.getSal() + self.__com
        print(f'HR salary = {final_sal}')

# Main Task
h1 = Hr(102, 'virat', 50000, 10000)
h1.display()
h1.calSal()