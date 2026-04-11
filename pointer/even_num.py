arr = [4, 7, 2, 9, 1]
count = 0

i = 0
while i < len(arr):
    if arr[i] % 2 == 0:
        count += 2
    i += 1

print(count)