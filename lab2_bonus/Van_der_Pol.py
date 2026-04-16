import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def vdp_deriv(t, Y, mu=50.0):
    """
    范德波尔振子 (Van der Pol oscillator) 微分方程
    d^2x/dt^2 - mu*(1 - x^2)*dx/dt + x = 0
    Y = [x, v]
    TODO: 补全导数计算，返回 [dx/dt, dv/dt]
    """
    pass

if __name__ == "__main__":
    # TODO: 物理参数 mu 可以从 1.0 增大到 50.0 观察 Stiffness (刚性) 的增强
    # TODO: 使用 RK45 和 Radau 求解器分别计算
    # TODO: 比较不同求解器在 mu=50.0 时的求解步数或所需时间 (nfev: number of function evaluations)
    # TODO: 绘制相图 (x-v) 观察极限环 (Limit Cycle)
    pass