#WAP to reverse the string without using slicing and inbuilt functions.
s = 'Rahul'

i = len(s) - 1
rev = ""

while i >= 0:
    rev = rev + s[i]
    i = i - 1

print("Reverse :", rev)