#Question 6: Write a program to calculate the third angle of a triangle if two angles are given.
angel1 = int(input(' Enter the first angel: '))
angel2 = int(input('enter the second angel: '))

angel3 = 180 - (angel1 + angel2)

print('Third angel of Triangle: ', angel3)