import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define x as a symbolic variable
x = sp.Symbol('x')

# Generate the Legendre polynomial using the recurrence relation
def legendre_poly(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2*n-1)*x*legendre_poly(n-1, x) - (n-1)*legendre_poly(n-2, x))/n

# Function for least squares approximation using the Legendre polynomials
def least_squares_approximation(f, basis, x):
    A = []
    b = []
    coeffs = sp.symbols(' '.join([f'c{i}' for i in range(len(basis))]))
    for bi in basis:
        A_row = [sp.integrate(bi*bj, (x, -1, 1)) for bj in basis]
        A.append(A_row)
        b.append(sp.integrate(f*bi, (x, -1, 1)))
    solution = sp.solve(sp.Matrix(A)*sp.Matrix(coeffs) - sp.Matrix(b), coeffs)
    approximation = sum([coeffs[i]*basis[i] for i in range(len(basis))]).subs(solution)
    return approximation

f = x * sp.exp(-x)
basis = [legendre_poly(i, x) for i in range(5)]
approximation = least_squares_approximation(f, basis, x)

# Plotting
x_vals = np.linspace(-1, 1, 400)
f_vals = [float(f.subs(x, val)) for val in x_vals]
approximation_vals = [float(approximation.subs(x, val)) for val in x_vals]

plt.figure(figsize=(10,6))
plt.plot(x_vals, f_vals, label='$f(x) = x e^{-x}$', color='blue')
plt.plot(x_vals, approximation_vals, label='Approximation', color='red', linestyle='--')
plt.title('Original Function vs. Legendre Polynomial Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
