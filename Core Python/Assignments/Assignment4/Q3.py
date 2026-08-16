#WAP to print sum of series upto n.
n = int(input('Enter N:'))
i = 1
sum = 0  
#Why is it used? This variable stores the running total.Initially, we haven't added any numbers.

while(i <= n):
    sum = sum + i
    i = i + 1
print('Sum : ', sum)    
