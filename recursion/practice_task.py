#Write a recursive function to 
#calculate sum of first n numbers

def calculate(n):
    if n == 1:
        return 1
    return n + calculate(n-1)

print(calculate(5))

# recursion example
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n-1)

print_numbers(5)