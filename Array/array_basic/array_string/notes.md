🔤 Strings — Short Notes

What is it?
-->A sequence of characters stored in quotes
s = "hello"
s = 'world'



#Indexing:
pythons = "hello"

print(s[0])    # 'h' → first character
print(s[-1])   # 'o' → last character



#Slicing:
pythons = "hello"

print(s[1:4])   # 'ell'  → index 1 to 3
print(s[:3])    # 'hel'  → start to index 2
print(s[2:])    # 'llo'  → index 2 to end
print(s[::-1])  # 'olleh' → reverse



#Common Methods:
pythons = "hello world"

print(s.upper())                     # HELLO WORLD
print(s.lower())                     # hello world
print(s.replace("world", "python"))  # hello python
print(s.split(" "))                  # ['hello', 'world']
print(s.count("l"))                  # 3
print(s.find("world"))               # 6
print(s.strip())                     # removes side spaces




#DSA Patterns:
pythons = "madam"

# Palindrome check
print(s == s[::-1])      # True

# Direct loop
for ch in s:
    print(ch)

# Index loop (when index + character both needed)
for i in range(len(s)):
    print(i, s[i])

# Length
print(len(s))            # 5




#⚡ Key Points:
ConceptDetailIndexings[0] → single characterSlicings[1:4] → multiple charactersReverses[::-1]Palindromes == s[::-1]Loopfor ch in s → direct character