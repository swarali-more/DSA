s = "madam"

# 1. Print length
print(len(s))

# 2. Print first and last character
print(s[0])
print(s[-1])

# 3. Check if palindrome
print(s == s[::-1])

# 4. Print string in reverse
print(s[::-1])

# 5. Print each character using loop
for ch in s:
    print(ch)