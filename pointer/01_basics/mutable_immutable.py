# =============================================
# 📁 mutable_immutable.py
# Topic: Mutable vs Immutable in Python
# =============================================

# -----------------------------------------------
# 1. Immutable - int (badlale tar nava object)
# -----------------------------------------------
a = 10
b = a
b = 20

print(a)    #10 -unchanged (immutable)
print(b)    #20 -chnaged
print(id(a) == id(b))   #False -new object added

# -----------------------------------------------
# 2. Mutable - list (same object badlto)
# -----------------------------------------------
a = [1,2,3]
b = a
b.append(4)

print(a)    #[1,2,3,4] -changed (mutable)
print(id(a) == id(b))   #True - same object!

#-----------------------------------------------
# 3. TRAP - b = [...] vs b.append()
# -----------------------------------------------
a = [1,2,3]
b = a

# Trap 1 -b.append() -changed same obj
b.append(4)
print(a)    #changed -(mutable)
print(id(a) == id(b))   #same address

# Trap 2 -b=[...] new list- b have new obj
b = [1,2,3,4,5]
print(a)       #[1,2,3,4] -unchanged -bcz now b have new obj
print(id(a) == id(b))   #False -(diffrent address)

# -----------------------------------------------
# 4. String - immutable (nava object banto)
# -----------------------------------------------
a = "hello"
b = a
b = b + "world"

print(a)    #unchanged -(immutable)
print(id(a) == id(b))   #False -b has new obj now!


