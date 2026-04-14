# ============================================================
# 02_memory/memory_model.py
# Python Memory Model — Stack, Heap, References
# ============================================================

import sys

# ── 1. Variable म्हणजे फक्त naam (label) ──────────────────
x = 42
y = x

print("=== Variables & References ===")
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"x is y → {x is y}")   # True — same object!
print()

# ── 2. Immutable — change = new object ────────────────────
print("=== Immutable (int) ===")
a = 100
print(f"Before: a = {a}, id = {id(a)}")
a = 200          # नवीन object, नवीन address
print(f"After:  a = {a}, id = {id(a)}")
print()

# ── 3. Mutable — in-place change ──────────────────────────
print("=== Mutable (list) ===")
list1 = [1, 2, 3]
list2 = list1             # same object कडे point
print(f"Before append: list2 = {list2}")
list1.append(99)
print(f"After  append: list2 = {list2}")   # list2 पण बदलला!
print(f"list1 is list2 → {list1 is list2}")
print()

# ── 4. id() — memory address ──────────────────────────────
print("=== id() — Object Identity ===")
p = "hello"
q = "hello"
print(f"p is q → {p is q}")   # True (string interning!)

r = [1, 2]
s = [1, 2]
print(f"r == s → {r == s}")   # True  (same value)
print(f"r is s → {r is s}")   # False (different objects)
print()

# ── 5. sys.getrefcount() — kitne references ahet ─────────
print("=== Reference Count ===")
my_obj = [10, 20, 30]
print(f"ref count = {sys.getrefcount(my_obj)}")  # 2 (my_obj + getrefcount arg)
alias = my_obj
print(f"ref count after alias = {sys.getrefcount(my_obj)}")  # 3
del alias
print(f"ref count after del  = {sys.getrefcount(my_obj)}")   # 2 परत
print()

# ── 6. None — special singleton ───────────────────────────
print("=== None is Singleton ===")
a = None
b = None
print(f"a is b → {a is b}")   # Always True — one None object