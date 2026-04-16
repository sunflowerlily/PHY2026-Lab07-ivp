import numpy as np
import matplotlib.pyplot as plt

def euler_step(f, y, t, dt):
    """
    实现前向欧拉法单步更新
    TODO: 补充前向欧拉法公式
    """
    pass

def rk4_step(f, y, t, dt):
    """
    实现四阶龙格-库塔法(RK4)单步更新
    TODO: 补充 RK4 的四个斜率 k1, k2, k3, k4 并返回下一个状态
    """
    pass

def harmonic_oscillator_deriv(t, Y):
    """
    简谐振子微分方程: d^2x/dt^2 = -omega^2 * x
    为了方便，我们取 omega = 1, 即 d^2x/dt^2 = -x
    设 Y = [x, v], 则返回导数 [dx/dt, dv/dt] = [v, -x]
    TODO: 补全此函数的返回值
    """
    pass

def calc_energy(Y):
    """
    计算简谐振子单位质量能量: E = 0.5 * v^2 + 0.5 * x^2 (omega=1)
    TODO: 补全能量计算
    """
    pass

if __name__ == "__main__":
    # 物理参数
    dt = 0.1
    t_max = 50.0
    times = np.arange(0, t_max, dt)
    
    # 初始状态：x(0) = 1.0, v(0) = 0.0
    Y0 = np.array([1.0, 0.0])
    
    # TODO: 初始化欧拉法和 RK4 法的存储数组，进行主循环积分
    
    # TODO: 绘制位移随时间变化图 (Euler vs RK4 vs 解析解 cos(t))
    # TODO: 绘制相图 (x-v) 观察能量发散/守恒情况
    # TODO: 绘制能量随时间变化图
    pass