def createlist(li):
    n = int(input('How many elements you want add:'))
    for i in range(n):
        ele = int(input('Enter element:'))
        li.append(ele)

li = []
createlist(li)
print(li)