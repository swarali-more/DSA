# ============================================================
# Double Pointer — List of Objects
# list → object → attribute  (2 levels of reference)
# ============================================================

class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f"Node({self.val})"

# List holds references to Node objects
nodes = [Node(10), Node(20), Node(30)]

print("nodes:", nodes)
print("nodes[1].val:", nodes[1].val)  # double deref

# -------------------------------------------------------
# Function च्या आत object modify करणे (double pointer effect)
# -------------------------------------------------------
def double_value(node_list, index):
    # list reference आहे, त्यामुळे object modify होते
    node_list[index].val *= 2

double_value(nodes, 1)
print("\nAfter double_value(nodes, 1):", nodes)
# → [Node(10), Node(40), Node(30)]

# -------------------------------------------------------
# Variable reassign vs object mutate — फरक
# -------------------------------------------------------
def wrong_replace(node):
    node = Node(999)        # local variable बदलली, original नाही
    print("  आत (wrong):", node)

def correct_replace(node_list, index):
    node_list[index] = Node(999)   # list च्या आत replace करतो
    print("  आत (correct):", node_list[index])

print("\n--- Replace test ---")
wrong_replace(nodes[0])
print("बाहेर (wrong):", nodes[0])   # unchanged

correct_replace(nodes, 0)
print("बाहेर (correct):", nodes[0]) # changed ✓

# -------------------------------------------------------
# Aliasing — दोन variables एकाच object ला point करतात
# -------------------------------------------------------
print("\n--- Aliasing ---")
a = Node(100)
b = a               # b → same object as a

b.val = 200
print("a.val:", a.val)   # 200 — कारण a आणि b एकच object
print("same object?", a is b)  # True