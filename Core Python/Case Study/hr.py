from Emp import Emp
class Hr(Emp):
    def __init__(self,id,name,sal,com):
        super().__init__(id,name,sal)
        self.com=com
    def calsal():
        print(f"Final Sal of HR={self.sal+self.com}")
    #def __str__(self):   
        #return super().__str__()+f"{self.com}"
