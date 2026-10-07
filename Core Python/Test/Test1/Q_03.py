#li = []

#for i in range(1,11):
#   li.append(i)

#print(li)    

#li = [1, 2, 3, 4, 5, 6, 7, 9]

#li1 = []

#for i in li:
#    li1.append(i**2)

#print(li1)    


#s = 'firstbit'

#print(s.upper())

#li = []
#for i in range(1,101):
#    if i%2!= 0:
#        li.append(i)
#print(li)    

#li = [i for i in range(1,101) if i%2!=0]
#print(li)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in li:
    if i%2==0:
        print("Even")
    else:
        print("odd")  

#
li = ["Even" if i%2==0 else "Odd" for i in range(1,11)]
print(li)


d = {}
for i in range (1,10):
    d[i]=i**2
print(d)    

dic={i:i*i for i in range(1,10)}
print(dic)




