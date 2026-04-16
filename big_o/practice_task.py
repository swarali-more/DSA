# Code 1
arr = [1, 2, 3, 4, 5]
print(arr[2])       #O(1)

# Code 2
for i in arr:
    print(i)        #O(n)

# Code 3
for i in arr:
    for j in arr:
        print(i, j)     #O(n2)

# Code 4
# Searching in a sorted array 
# by cutting it in half each step
#ans-->#O(log n)


