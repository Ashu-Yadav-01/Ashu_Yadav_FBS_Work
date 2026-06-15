#Question 1: Write a program to calculate the percentage of a student based on marks of any 5 subjects
sub1 = float(input('Enter marks of Maths:'))
sub2 = float(input('Enter marks of English:'))
sub3 = float(input('Enter marks of Marathi:'))
sub4 = float(input('Enter marks of Hindi:'))
sub5 = float(input('Enter marks of Science'))

total = sub1 + sub2 + sub3 + sub4 + sub5 
percentage = (total / 500) * 100

print('Total Marks =', total)
print('Percentage =', percentage)