import time
f=open("file.txt",'r+')
print(f.tell())
f.write("I am good in Python")
print(f.tell())
f.seek(2)
print(f.read())