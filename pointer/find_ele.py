arr = [4, 7, 2, 9, 1]
target = 9

i = 0
found = False

while i < len(arr):
    if arr[i] == target:
        found = True
        break
    i += 1

print("Found" if found else "Not Found")