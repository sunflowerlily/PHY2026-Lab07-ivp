import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ==========================================
# ⚠️ AI 生成的草稿代码 (包含有意为之的物理和语法 BUG)
# ==========================================

def lorenz_deriv(t, state, sigma, rho, beta):
    """
    计算洛伦兹吸引子的导数。
    状态向量 state = [x, y, z]
    """
    x, y, z = state
    # 故意留下的BUG 1：物理方程的符号写错了（请回顾讲义或查找资料纠正）
    dx = sigma * (y + x) 
    dy = x * (rho - z) - y
    dz = x * y + beta * z 
    return [dx, dy, dz]

def solve_lorenz():
    """
    调用 scipy.integrate.solve_ivp 求解
    """
    # 初始条件和参数
    y0 = [1.0, 1.0, 1.0]
    t_span = (0, 50)
    t_eval = np.linspace(0, 50, 5000)
    sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
    
    # 故意留下的BUG 2：solve_ivp 的参数传递方式错误
    # 注意 scipy 中如何传递额外的 args 给微分方程
    # sol = solve_ivp(lorenz_deriv, t_span, y0, t_eval=t_eval) # 运行这行会报错！
    
    # TODO: 修正上述方程中的物理符号
    # TODO: 修正 solve_ivp 的调用，并正确获取求解结果
    
    # TODO: 绘制 3D 轨迹图 (x, y, z) 
    # TODO: 绘制时序图 x(t)
    pass

if __name__ == "__main__":
    solve_lorenz()
