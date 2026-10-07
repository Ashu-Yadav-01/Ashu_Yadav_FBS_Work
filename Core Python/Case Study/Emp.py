from abc import ABC,abstractmethod
class Emp(ABC):
    def __init__(self,id,name,sal):
        self.id==id
        self.name=name
        self.sal= sal
    @abstractmethod      
    def calSal():
        pass
    def __str__(self):
        return f"Id={self.id}\+ name={self.name}\+ sal={self.sal}"