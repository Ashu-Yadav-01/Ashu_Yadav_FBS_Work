def binarySearch(li, search_ele):
    beg = 0
    end = len(li) - 1

    while beg <= end:
        print("while...")
        mid = (beg + end) // 2

        if search_ele == li[mid]:
            return mid
        elif search_ele < li[mid]:
            end = mid - 1
        else:
            beg = mid + 1

    return -1


li = [10, 20, 30, 40, 50, 60, 70]

ele = int(input("Enter element to search: "))

res = binarySearch(li, ele)

if res != -1:
    print(f"{ele} is found at index {res}")
else:
    print(f"{ele} is not available")