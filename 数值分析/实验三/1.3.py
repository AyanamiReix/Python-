import numpy as np
import sympy as sp

x = sp.Symbol('x')

# 生成勒让德多项式
def legendre_poly(n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2*n-1)*x*legendre_poly(n-1) - (n-1)*legendre_poly(n-2))/n

# 生成切比雪夫多项式
def chebyshev_poly(n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return 2*x*chebyshev_poly(n-1) - chebyshev_poly(n-2)

# 计算两个函数的内积
def inner_product(f, g):
    return sp.integrate(f * g, (x, -1, 1))

# 最佳平方逼近
def least_squares_approximation(f, basis):
    b = [inner_product(f, phi) for phi in basis]
    A = [[inner_product(phi_i, phi_j) for phi_j in basis] for phi_i in basis]
    coeffs = sp.symbols(f'c:{len(basis)}')  # 定义系数变量
    solution = sp.solve(sp.Matrix(A) * sp.Matrix(coeffs) - sp.Matrix(b), coeffs)
    approximation = sum(solution[c]*phi for c, phi in zip(coeffs, basis))
    return approximation


f = x * sp.exp(-x)
legendre_basis = [legendre_poly(i) for i in range(5)]
approximation = least_squares_approximation(f, legendre_basis)

print("4次最佳平方逼近多项式：", approximation)

error_squared = sp.integrate((f - approximation)**2, (x, -1, 1))
print("均方误差：", sp.sqrt(error_squared))

errors = []

# Debugging: 检查f和approximation
problematic_vals = []
for val in np.linspace(-1, 1, 1000):
    f_val = f.evalf(subs={x: val})
    approx_val = approximation.evalf(subs={x: val})

    if not isinstance(f_val, (int, float, sp.Integer, sp.Float)) or not isinstance(approx_val, (int, float, sp.Integer, sp.Float)):
        problematic_vals.append((val, f_val, approx_val))
    else:
        errors.append(abs(f_val - approx_val))

print("最大误差：", max(errors))

if errors:
    print("最大误差：", max(errors))
else:
    print("无法计算误差！")

if problematic_vals:
    print("\n以下是评估f和approximation时出现问题的点：")
    for val, f_val, approx_val in problematic_vals:
        print(f"At x = {val}:")
        print("f:", f_val)
        print("approximation:", approx_val)
else:
    print("\nf和approximation在所有点上都被成功评估!")
