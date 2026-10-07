def linearSearch(li, searchEle):
    for i in range(0, len(li)):
        if(li[i] == searchEle):
            return 1
        else:
            return -1
        
ele = 80
li = [10, 20, 30, 40, 50, 60, 70]
res = linearSearch(li, ele)
if(res != -1):
    print(f'{ele} is present')        