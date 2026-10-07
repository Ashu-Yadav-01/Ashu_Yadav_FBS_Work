class Student:
    def __init__(self, rn, name, marks):
        self.__rollno = rn
        self.__name = name
        self.__marks = marks

    def __str__(self):
        return f"Id= {self.__rollno}\t Name={self.__name}\tMarks= {self.__marks}"

s1 = Student(22, "Rohit", 32)
print(s1)