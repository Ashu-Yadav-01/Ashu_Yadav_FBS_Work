import pickle
class Emp:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal
        
    def __str__(self):
        return f"{self.id},{self.name},{self.sal}"
e1 = Emp(12,"MSD",123321)
#f = open("FilePath", Model)
#f=open("Emp.dat","wb")
with open("Emp.dat","wb") as f:
    pickle.dump(e1,f)
    pickle.dump(Emp(10,"Sachin",23432),f)
    pickle.dump(Emp(1,"Rahul",2345),f)
with open("Emp.dat","rb") as f:
    while True:
        try:
            data=pickle.load(f)
            print(data)
        except EOFError as e:
            print("Sara Data Khatam")
            break    







