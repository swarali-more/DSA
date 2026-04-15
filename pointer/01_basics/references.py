# -----------------------------------------------
# 1. id() - Memory Address
# -----------------------------------------------
a = 10
print(id(a))    #memory address ofobject 10

# -----------------------------------------------
# 2. b = a - Same object, two labels
# -----------------------------------------------
a = 10
b = a
print(id(a) == id(b))   #same object

# -----------------------------------------------
# 3. int is - (immutable)
# -----------------------------------------------
b = 20
print(a)    #10 unchanged
print(id(a) == id(b))   #False - new object

# -----------------------------------------------
# 4. List is - (mutable)
# -----------------------------------------------
a =[1,2,3]
b = a
b.append(4)

print(a)     # [1, 2, 3, 4] - a pan badlala!
print(id(a) == id(b))   #True - same object

# -----------------------------------------------
# 5. is vs ==
# -----------------------------------------------

# Always use: is None
# Never use: == None

a = [1,2,3]
b = a
c = [1,2,3]

print(a == c)
print(a is c)
print(a == b)
print(a is b)
print(b == c)
print(b is c)

# -------------------------------------------------------
# 7. sys.getrefcount()
# -------------------------------------------------------

import sys

a = [1, 2, 3]

print(sys.getrefcount(a))   # 2 (a + function argument)

b = a
print(sys.getrefcount(a))   # 3 (a + b + function argument)

del b
print(sys.getrefcount(a))   # 2 (back)


# -------------------------------------------------------
# 8. None - singleton
# -------------------------------------------------------

x = None
y = None

print(x is y)   # True (same object)
print(x == y)   # True (but 'is' preferred)