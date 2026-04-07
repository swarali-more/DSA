📏 len() — Short Notes

What is it?
-->Returns the number of elements in any sequence

Syntax:
len(object)

Examples:
# List
arr = [10, 20, 30]
print(len(arr))      # 3

# String
s = "hello"
print(len(s))        # 5

# Empty
print(len([]))       # 0

DSA Usage:
arr = [5, 10, 15, 20]

len(arr)              # 4  → size
arr[len(arr) - 1]     # 20 → last element
range(len(arr))       # 0,1,2,3 → for loops

⚡ Key Points:
Speed   --   O(1) — instant
Works on  -- List, String, Tuple, Dict, Set
Common use  -- Loop, last index, size check