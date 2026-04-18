# ============================================================
# Double Pointer in Python — Nested List
# outer list → inner lists → values (2 levels of reference)
# ============================================================

# C मध्ये:  int **ptr  →  int *arr  →  int value
# Python मध्ये: outer   →  inner    →  value  (same concept!)

# Basic nested list
outer = [[1, 2], [3, 4]]

print("outer     :", outer)
print("outer[0]  :", outer[0])      # inner list (first pointer deref)
print("outer[0][1]:", outer[0][1])  # actual value (second pointer deref)

# -------------------------------------------------------
# Mutation — outer च्या आत जाऊन inner बदलणे
# -------------------------------------------------------
outer[1][0] = 99
print("\nouter[1][0] = 99 केल्यावर:", outer)
# → [[1, 2], [99, 4]]

# -------------------------------------------------------
# Common trap — shallow copy
# -------------------------------------------------------
print("\n--- Shallow Copy Trap ---")

rows = 2
cols = 2

# ❌ WRONG — सगळ्या rows एकाच list ला point करतात
wrong_grid = [[0] * cols] * rows
wrong_grid[0][0] = 5
print("Wrong grid:", wrong_grid)
# → [[5, 0], [5, 0]]  ← दोन्ही rows बदलल्या! (same reference)

# ✅ CORRECT — list comprehension ने नवी list बनते
correct_grid = [[0] * cols for _ in range(rows)]
correct_grid[0][0] = 5
print("Correct grid:", correct_grid)
# → [[5, 0], [0, 0]]  ← फक्त row 0 बदलली

# -------------------------------------------------------
# id() ने references तपासणे
# -------------------------------------------------------
print("\n--- id() check ---")
print("wrong_grid row ids:", id(wrong_grid[0]), id(wrong_grid[1]))
# same id → same object!

print("correct_grid row ids:", id(correct_grid[0]), id(correct_grid[1]))
# different id → different objects ✓