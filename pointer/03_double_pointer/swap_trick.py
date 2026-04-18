# ============================================================
# Double Pointer — Swap Trick
# Python मध्ये function च्या आत values swap करण्यासाठी
# list wrapper (container) वापरतो
# ============================================================

# -------------------------------------------------------
# ❌ Direct swap — काम करत नाही
# -------------------------------------------------------
def wrong_swap(a, b):
    a, b = b, a
    print(f"  function आत: a={a}, b={b}")  # swapped locally

x, y = 10, 20
wrong_swap(x, y)
print(f"बाहेर: x={x}, y={y}")  # ← unchanged! integers immutable आहेत

# -------------------------------------------------------
# ✅ List wrapper swap — काम करते (double pointer trick)
# -------------------------------------------------------
def correct_swap(wrap_a, wrap_b):
    # wrap_a[0] = container च्या आत जाऊन value बदलणे
    wrap_a[0], wrap_b[0] = wrap_b[0], wrap_a[0]
    print(f"  function आत: wrap_a={wrap_a}, wrap_b={wrap_b}")

wrap_x = [10]
wrap_y = [20]
correct_swap(wrap_x, wrap_y)
print(f"बाहेर: wrap_x={wrap_x}, wrap_y={wrap_y}")  # ← swapped! ✓

# -------------------------------------------------------
# Real use case — multiple return values (Python चा proper way)
# -------------------------------------------------------
print("\n--- Python चा proper way ---")

def swap_and_return(a, b):
    return b, a   # tuple unpack

p, q = 100, 200
p, q = swap_and_return(p, q)
print(f"p={p}, q={q}")  # p=200, q=100 ✓

# -------------------------------------------------------
# Object attribute swap — double pointer effect
# -------------------------------------------------------
print("\n--- Object attribute swap ---")

class Box:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return f"Box({self.val})"

def swap_attrs(box1, box2):
    # objects mutable आहेत, directly attribute swap होते
    box1.val, box2.val = box2.val, box1.val

b1 = Box(111)
b2 = Box(222)
print("Before:", b1, b2)
swap_attrs(b1, b2)
print("After:", b1, b2)   # Box(222) Box(111) ✓

# -------------------------------------------------------
# Summary — कधी काय वापरायचे
# -------------------------------------------------------
print("""
Summary:
  int/str swap बाहेर करायचा  → simple a, b = b, a
  function आत int swap करायचा → list wrapper [val] वापर
  objects swap करायचे         → attribute swap directly होते
""")