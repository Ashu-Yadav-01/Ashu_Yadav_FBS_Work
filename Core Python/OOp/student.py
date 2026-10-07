class Student:
    collageName="FBs"
    @staticmethod
    def greet():
        print(f"Well Come to {Student.collageName}")
    def __init__(self,RollNo,name,marks):
        self.rollno=RollNo
        self.name=name
        self.marks=marks
    def getRollNo(self):
        return self.rollno
    def setRollNo(self,rn):
        self.rollno=rn

    def getName(self):
        return self.name