Part 1: Basic Concept

What is Recursion?
-->A function that calls itself until a condition is met

def countdown(n):
    if n == 0:
        print("Done")
        return
    print(n)
    countdown(n - 1)

countdown(3)
Output:
3
2
1
Done

Part 2: Base Case & Recursive Case

Base Case:
-->Tells function when to stop — without this infinite loop occurs

if n == 0:      # Base Case
    return      # stop!

Recursive Case:
-->Function calls itself — carries work forward

countdown(n - 1)   # Recursive Case


Rule:
No Base Case → infinite loop → program crash
No Recursive Case → not recursion


Part 3: How it works internally?

Stack:

Every function call goes on top of stack — one above another

countdown(3) → on stack
    countdown(2) → on stack
        countdown(1) → on stack
            countdown(0) → STOP
        countdown(1) → finish
    countdown(2) → finish
countdown(3) → finish
Real life analogy:

Like a stack of plates —

Last plate placed → first plate removed
This is LIFO — Last In First Out



Example — Factorial:

def factorial(n):
    if n == 1:                    # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print(factorial(5))   # 120


Simple Rule:
Use recursion when problem naturally repeats itself — like folders inside folders, branches in a tree!

