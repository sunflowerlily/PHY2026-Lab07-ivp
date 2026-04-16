import numpy as np
from lab2_bonus.Van_der_Pol import vdp_deriv

def test_vdp_deriv():
    """
    测试范德波尔振子导数
    mu = 50.0, x=2.0, v=1.0
    d^2x/dt^2 = mu*(1 - x^2)*v - x = 50 * (1 - 4) * 1 - 2 = -152
    """
    Y = np.array([2.0, 1.0])
    dY = vdp_deriv(0.0, Y, mu=50.0)
    
    expected_dY = np.array([1.0, -152.0])
    assert np.allclose(dY, expected_dY), "Van der Pol 导数计算错误"