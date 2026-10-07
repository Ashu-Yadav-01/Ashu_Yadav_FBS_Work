class Student:
    # collegeName = "FBS"
    # @staticmethod
    # def greet():
    #     print(f"Well come to {Student.collegeName}")
    def __init__(self,RollNo, name, marks):
        self.rollno = RollNo
        self.name = name
        self.marks = marks

    def getRollNo(self):
        return self.rollno
    def setRollNo(self,rn):
        self.rollno = rn

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

    def getMarks(self):
        return self.marks
    def setMarks(self,marks):
        self.marks = marks

    def display(self):
        print(f"Roll No. : {self.rollno} \tName : {self.name} \tMarks : {self.marks}")

class PlaceStudent(Student):
    def __init__(self, RollNo, name, marks,sal):
        super().__init__(RollNo, name, marks)
        self.sal = sal

    def display(self):
        print(f"Salary : {self.sal}",end=" ")
        print()

        return super().display()
    

s3 = PlaceStudent(103, "Amit", 49 , 1000)
print()
s1 = Student(101, "Rohit", 45)
s2 = Student(102, "Rohan", 47)

PlaceStudent.display(s3)
print()
Student.display(s1)
print()
Student.display(s1)