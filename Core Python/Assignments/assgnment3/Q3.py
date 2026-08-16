#Write a program to input angles of a triangle and check whether triangle is valid or not.
a = int(input('Enter the angle A: '))
b = int(input('Enter the angle B: '))
c = int(input('Enter the angle C: '))

sum = a + b + c

if sum == 180 and a > 0 and b > 0 and c > 0 :
    print('Triangle is valid',sum)
else:
    print('Triangle is valid',sum)
   
