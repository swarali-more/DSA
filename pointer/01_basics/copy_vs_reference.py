# =============================================
# 📁 copy_reference.py
# Topic: Copy vs Reference in Python
# =============================================

# -----------------------------------------------
# 1. Reference - same object
# -----------------------------------------------
a = [1,2,3]
b = a

b.append(4)
print(id(a) == id(b))   #b is a shortcut - same object!

# -----------------------------------------------
# 2. Shallow Copy - outer level new, inner is same
# -----------------------------------------------
a = [1,2,3]
b =a.copy()     #new outer list

b.append(4)

print(a)    #still safe
print(id(a) == id(b))   #False -differnt obj

# -----------------------------------------------
# 3. Shallow Copy TRAP - nested list
# -----------------------------------------------
a =[[1,2],[3,4]]
b = a.copy()    #outer list new, inner still same

print(a)
print(b)

b[0].append(99) #[[1, 2, 99], [3, 4]] - a is also changed!(muttable)

print(a)
print(b)

print(id(a) == id(b))

# -----------------------------------------------
# 4. Deep Copy - completely swatantra
# -----------------------------------------------
import copy

a = [[1,2] , [3,4]]
b = copy.deepcopy(a)    #all new objects!

b[0].append(99) 

print(a)    # [[1, 2], [3, 4]] - safe!
print(id(a[0]) == id(b[0])) #False -inner obj are aslo different