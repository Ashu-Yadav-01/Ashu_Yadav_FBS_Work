from userdefine_1 import FbsException
def ShowEmp(id, name, age):
    try:
        if age<18 and age>79:
            raise FbsException(age)
    except Exception as a:
        print(a)
    print(f"Id={id}\t Name={name}\t age={age}")  

id = input("Enter Emp ID:")
name=input("Enter Emp Name:")
age=int(input("Enter th age:2"))
ShowEmp(id,name,age)



    