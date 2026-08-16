#WAP to print all numbers in a range divisible by a given number.
Start = int(input("Enter Starting number : "))
end = int(input("Enter Ending number : "))
num = int(input("Enter number : "))

i = Start

while i <= end:
    if i % num == 0 :
        print(i, end=" ")

    i = i + 1    