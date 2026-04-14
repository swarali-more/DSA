 Big O 
 1."Big O notation describes how the number of operations in an algorithm grows as the input size increases. It helps us compare algorithms and choose the most efficient one.

 2.For example, a single loop is O(n) — if input doubles, operations double. But a nested loop is O(n²) — if input doubles, operations quadruple

 3.keywords:
    "grows as input size increases"
    "number of operations"
    "helps compare algorithms"


O(1) — Constant:
print(arr[0])

n = 10 → 1 operation
n = 1000 → 1 operation
Size doesn't matter!

O(n) — Linear:
for i in arr:
    print(i)

n = 10 → 10 operations
n = 1000 → 1000 operations

O(n²) — Quadratic:
for i in arr:
    for j in arr:
        print(i, j)

n = 10 → 100 operations
n = 1000 → 1,000,000 operations

O(log n) — Logarithmic:
# Binary Search

n = 1000 → only 10 operations
Each step cuts problem in half!


Speed Order:
Fast → Slow
O(1) > O(log n) > O(n) > O(n²)



# Big-O Notes

O(1) - Constant
O(n) - Linear
O(n^2) - Quadratic

Example:
Loop = O(n)
Nested loop = O(n^2)