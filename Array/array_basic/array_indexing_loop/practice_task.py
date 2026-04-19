##Q1 - Create an array of 5 fruits and print the last fruit

fruits = ["Apple","Banana","Mango"]
print(fruits[-1])

##Q2 - Print only the 3rd element of this array

arr = [10, 20, 30, 40, 50]
print(arr[2])

##Q3 - Print all elements of this array using a loop

arr = ["apple", "banana", "mango"]
for i in arr:
    print(i)

##Print each element with its index

arr = [10, 20, 30, 40]
for i in range(len(arr)):
    print(i,arr[i])


# array indexing and loop example

arr = [10, 20, 30, 40]

for i in range(len(arr)):
    print(f"Index {i} -> {arr[i]}")

