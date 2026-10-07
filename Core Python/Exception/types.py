num1 = int(input("Enter the number1:"))
num2 = int(input("Enter the number1: "))

try:
    print(num1/num2)
    no=int(input("Enter the number:"))
    li = [12,10]
    print(li[4])
except ZeroDivisionError as z:
    print(z)
    print("Denomenator me zero nahi ho sakta")
except ValueError as v:
    print(v)
    print("please Enter in it")
except IndentationError as i:
    print(i)
    print("I am index error ")
except Exception as e:
    print(e)
    print("Generlize")   
else:
    print("All Good...............")     
finally:
    print("I am in finally block")                