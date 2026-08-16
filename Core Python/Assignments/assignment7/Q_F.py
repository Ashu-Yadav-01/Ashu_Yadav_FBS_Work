row = 5

i = 1
while i <= row:


    j = i 
    while j <= row:


        if i == 1 or j == i or j == row:
            print(j, end=" ")
        else:
            print("  ", end="")    

        j = j + 1

    print()
    i = i + 1            