''' Write a program to check if given number is Armstrong number or not.
(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
4*4*4*4)  '''

n = int(input("Enter number: "))

original = n
temp = n
count = 0


while temp > 0:
    count = count + 1
    temp = temp // 10

sum = 0
temp = n


while temp > 0:

    digit = temp % 10

    power = 1
    i = 1

    while i <= count:
        power = power * digit
        i = i + 1

    sum = sum + power

    temp = temp // 10

if sum == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")  