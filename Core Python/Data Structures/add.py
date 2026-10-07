li = [34, 57, 83, 42, 23, 53, 65]

sum = 0 

#Method1
# for val in li:
#     sum += val

## Method2 : Indexing 
for i in range(len(li)):
    sum += li[i]

print(sum)    