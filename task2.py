def golden_section(f, a, b, tol):
    phi = (1 + 5**0.5) / 2  # Golden ratio
    resphi = 2 - phi
    c = a + resphi * (b - a)
    d = b - resphi * (b - a)
    
    while abs(b - a) > tol:
        if f(c) < f(d):
            b = d
            d = c
            c = a + resphi * (b - a)
        else:
            a = c
            c = d
            d = b - resphi * (b - a)
    
    xmin = (a + b) / 2
    return xmin, f(xmin)

# Define the function
f = lambda x: (x - 2)**2 + 3

#Inputs
a, b = map(int,input().split())
tol = float(input())

# Test with the interval [0, 5] and tolerance 10^(-4)
xmin, fmin = golden_section(f, a, b, tol)
print(f"Minimum at x = {xmin}, f(x) = {fmin}")
