from math import e
def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at endpoints a and b.")
    
    iteration = 0
    while True:
        c = (a + b) / 2  # Midpoint
        fc = func(c)
        
        print(f"Iteration {iteration}: a = {a}, b = {b}, c = {c}, f(c) = {fc}")
        
        # Check if the midpoint is the root or close enough
        if abs(fc) < tol:
            return c

        # Narrow the interval
        if func(a) * fc < 0:
            b = c
        else:
            a = c
        
        iteration += 1

# Define the function
def f(x):
    return x**3 - 6*x**2 + 11*x - 6

# Inputs
a, b = map(int,input().split())
tol = float(input())
# Find the root
try:
    root = bisection_method(f, a, b, tol)
    print(f"\nApproximate root: {root}")
except ValueError as e:
    print(e)
