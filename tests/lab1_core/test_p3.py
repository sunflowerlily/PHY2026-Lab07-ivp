import numpy as np
from lab1_core.P3_Kepler_Orbit.p3_kepler import kepler_deriv, calc_angular_momentum

def test_kepler_deriv_circular():
    """
    测试圆形轨道下的加速度计算。
    r = 1.0, GM = 1.0 -> v = 1.0
    x=1.0, y=0.0 -> a_x = -1.0, a_y = 0.0
    """
    Y = np.array([1.0, 0.0, 0.0, 1.0])
    dY = kepler_deriv(0.0, Y)
    
    # [vx, vy, ax, ay]
    expected_dY = np.array([0.0, 1.0, -1.0, 0.0])
    assert np.allclose(dY, expected_dY), "开普勒二体问题导数计算错误"

def test_angular_momentum():
    """
    测试角动量计算 L = x*vy - y*vx
    """
    Y = np.array([2.0, 0.0, 0.0, 1.5]) # x=2, vy=1.5
    L = calc_angular_momentum(Y)
    assert np.isclose(L, 3.0), f"角动量计算错误: expected 3.0, got {L}"