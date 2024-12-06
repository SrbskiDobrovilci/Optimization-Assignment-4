def gradient_ascent(derivative, x0, alpha, iterations):
    x = x0
    for i in range(iterations):
        grad = derivative(x)
        x = x + alpha * grad
        print(f"Iteration {i + 1}: x = {x}, f'(x) = {grad}")
    
    return x, (-x**2 + 4*x + 1)  # Calculate f(x)

# Define the derivative of f(x)
def df(x):
    return -2*x + 4

# Inputs
x0 = float(input())  # Initial guess
alpha = float(input())  # Learning rate
iterations = int(input())  # Number of iterations

# Perform Gradient Ascent
xmax, f_xmax = gradient_ascent(df, x0, alpha, iterations)
print(f"\nApproximate xmax: {xmax}")
print(f"f(xmax): {f_xmax}")
