li = [34, 57, 83, 42, 23, 53, 65]

max = li[0]
for i in range(1, len(li)):
    if(li[i] > max):
        max = li[i]

    print('Maximum number:', max)    
    