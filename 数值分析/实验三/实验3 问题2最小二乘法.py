import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# 数据
t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([0.01, 0.61, 1.13, 1.56, 1.84, 2.07, 2.18, 2.22, 2.23])

# 1. 绘制散点图
plt.scatter(t, y, label="数据点", color="red")
plt.xlabel('时间 (小时)')
plt.ylabel('浓度 (摩尔/升)')
plt.title('浓度与时间')
plt.grid(True)

# 定义拟合函数
# 一次函数
def linear(t, a, b):
    return a * t + b

# 二次函数
def quadratic(t, a, b, c):
    return a * t**2 + b * t + c

# 三次函数
def cubic(t, a, b, c, d):
    return a * t**3 + b * t**2 + c * t + d

# 进行数据拟合
popt_linear, _ = curve_fit(linear, t, y)
popt_quadratic, _ = curve_fit(quadratic, t, y)
popt_cubic, _ = curve_fit(cubic, t, y)

t_dense = np.linspace(0, 11, 400)
plt.plot(t_dense, linear(t_dense, *popt_linear), label="线性拟合")
plt.plot(t_dense, quadratic(t_dense, *popt_quadratic), label="二次拟合")
plt.plot(t_dense, cubic(t_dense, *popt_cubic), label="三次拟合")

# 预测给定时间点的浓度
t_predict = np.array([9, 10, 11])
y_actual = np.array([2.24, 2.25, 2.25])
y_linear = linear(t_predict, *popt_linear)
y_quadratic = quadratic(t_predict, *popt_quadratic)
y_cubic = cubic(t_predict, *popt_cubic)

# 计算平方误差
mse_linear = np.mean((y_actual - y_linear)**2)
mse_quadratic = np.mean((y_actual - y_quadratic)**2)
mse_cubic = np.mean((y_actual - y_cubic)**2)

print(f"线性拟合预测值: {y_linear}，均方误差: {mse_linear:.4f}")
print(f"二次拟合预测值: {y_quadratic}，均方误差: {mse_quadratic:.4f}")
print(f"三次拟合预测值: {y_cubic}，均方误差: {mse_cubic:.4f}")

plt.legend()
plt.show()
