import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def kepler_deriv(t, Y):
    """
    开普勒二体问题（简化为单体在中心力场中的运动）
    r'' = - (G*M / r^3) * r 矢量
    为了方便，取 GM = 1
    Y = [x, y, vx, vy]
    TODO: 补全导数计算
    """
    pass

def calc_angular_momentum(Y):
    """
    计算角动量 L = x*vy - y*vx
    TODO: 补全角动量计算
    """
    pass

def calc_runge_lenz(Y):
    """
    计算龙格-楞次矢量 (Runge-Lenz vector) 标量大小或矢量分量
    A = p x L - mk (此处 GM=1)
    TODO: 补全计算
    """
    pass

if __name__ == "__main__":
    # TODO: 设定初始条件，确保轨道是一个椭圆
    # TODO: 调用 solve_ivp (RK45) 求解轨道
    # TODO: 绘制轨道图
    # TODO: 绘制能量、角动量随时间的变化曲线，观察其守恒性
    pass