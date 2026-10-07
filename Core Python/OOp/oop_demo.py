class Emp:

    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def display(self):
        print(f"ID={self.id}\t Name={self.name}\t Salary={self.sal}")

e1 = Emp(101, "Sachin", 1220022)

print(id(e1))

e1.display()