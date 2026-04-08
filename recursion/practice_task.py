#Write a recursive function to 
#calculate sum of first n numbers

def calculate(n):
    if n == 1:
        return 1
    return n + calculate(n-1)

print(calculate(5))