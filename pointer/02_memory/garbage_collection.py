import sys
import gc

# ── 1. Basic refcount ──────────────────────────────────────
a = [1, 2, 3]
print(sys.getrefcount(a))  # 2 (a + argument)

b = a
print(sys.getrefcount(a))  # 3 (a + b + argument)

del b
print(sys.getrefcount(a))  # 2 back

del a
# refcount = 0 → object deleted from heap

# ── 2. Cycle problem ───────────────────────────────────────
x = []
y = []
x.append(y)   # x holds y
y.append(x)   # y holds x

del x
del y
# both still in memory! refcount = 1 each

# ── 3. Fix cycle with gc ───────────────────────────────────
gc.collect()
print("cycle cleaned!")

# ── 4. How many objects gc is tracking ────────────────────
print(gc.get_count())  # (gen0, gen1, gen2)