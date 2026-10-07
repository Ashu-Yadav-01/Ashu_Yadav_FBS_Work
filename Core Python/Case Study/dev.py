from Emp import Emp
class Dev(Emp):
    def __init__(self,id,name,sal,bonus):
        super().__init__(id,name,sal)
        self.bonus=bonus

    def calSal(self):
        print(f"Final Sal of HR={self.sal+self.com}")
    def __str__(self):
        return f"Id={self.id}\+ Name={self.name} Sal={self.sal}\+ Bonus={self.com}"    
    
