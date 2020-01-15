# Recursive Search
def recursiveSearch (array, left, right, x):
    if right >= left:
        middle = left + (right - left)/2
        if array[int(middle)] == x:
            return middle
        elif array[int(middle)] > x:
            return recursiveSearch(array, left, middle - 1, x)
        else:
            return recursiveSearch(array, middle + 1, right, x)
    else:
        return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x = 5

print("The recursive search is below...")
results = recursiveSearch(array, 0, len(array)-1, int(input("Number please: ")))
print(array)

if results != -1:
    print(f"Your requested item is present at %d" % results)
else:
    print("Your requested item is not found in this array.")



#Iterative Search
def iterativeSearch (arr, l, r, y):
    while l <= r:
        mid = l + (r - l)/2
        if arr[int(mid)] == y:
            return mid
        elif arr[int(mid)] < y:
            l = mid + 1
        else:
            r = mid - 1
    return -1

arr = list(range(1,1000))
y = 6

print("\nIterative search below...")
result = iterativeSearch(arr, 0, len(arr)-1, int(input("Another Number please in a different array: ")))
# print(arr)

if result != -1:
    print(f"The item you requested is in %d" % result)
else:
    print("The requested item is not in this array...")
