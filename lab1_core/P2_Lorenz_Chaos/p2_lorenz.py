import numpy as np
import matplotlib.pyplot as plt

def lorenz_deriv(t, Y, sigma=10.0, rho=28.0, beta=8.0/3.0):
    """
    洛伦兹吸引子微分方程
    dx/dt = sigma * (y - x)
    dy/dt = x * (rho - z) - y
    dz/dt = x * y - beta * z
    """
    x, y, z = Y
    # 【AI 陷阱】此处代码有两处物理/数学错误！
    # 请找出错误并修正它。
    # 错误 1: rho - z 写成了 rho + z
    # 错误 2: beta * z 写成了 beta / z (或者漏掉了负号)
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho + z) - y   # FIXME: AI 生成的代码这里符号错误
    dz_dt = x * y - beta / z    # FIXME: AI 生成的代码这里符号错误
    return np.array([dx_dt, dy_dt, dz_dt])

# TODO: 利用 scipy.integrate.solve_ivp 求解该方程
# TODO: 绘制 3D 洛伦兹吸引子轨迹 (Butterfly Effect)
# TODO: 探究初值敏感性 (微小扰动 1e-5 导致的轨迹偏离)

if __name__ == "__main__":
    pass