#problem: 1
#Given a string, check if it is a palindrome or not
 
s = "racecar"

if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


#Using result variable:
result = s == s[::-1]
print(result)


#Problem: 2
# Count vowels in a string
s = "hello world" 
count = 0

for ch in s:
    if ch in "aeiou":
        count+=1
print(count)



#Problem : 3
#Given a string, print all characters in uppercase and check if length > 5
s = "python world"
print(s.upper())

if len(s)> 5:
    print("Length is greater than 5")
else:
    print("Length is not greater than 5")


#Given a string, check if it starts with a vowel or consonant
s= "apple"
if s[0] in "aeiou":
    print("Starts with a vowel")
else:
    print("Starts with a consonant")


