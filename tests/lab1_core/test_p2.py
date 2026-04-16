import numpy as np
from lab1_core.P2_Lorenz_Chaos.p2_lorenz import lorenz_deriv

def test_lorenz_deriv():
    """
    测试学生是否修复了 AI 生成的洛伦兹方程错误。
    正确的导数：
    x=1, y=2, z=3, sigma=10, rho=28, beta=8/3
    dx/dt = 10*(2-1) = 10
    dy/dt = 1*(28-3) - 2 = 23
    dz/dt = 1*2 - (8/3)*3 = -6
    """
    Y = np.array([1.0, 2.0, 3.0])
    t = 0.0
    dY = lorenz_deriv(t, Y)
    
    expected_dY = np.array([10.0, 23.0, -6.0])
    
    # 检查误差
    assert np.allclose(dY, expected_dY), "洛伦兹方程的导数计算错误！请检查 AI 生成的代码陷阱。"