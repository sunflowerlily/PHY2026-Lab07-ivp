import numpy as np
from lab1_core.P1_Harmonic_Oscillator.p1_harmonic import rk4_step, harmonic_oscillator_deriv, calc_energy

def test_rk4_energy_conservation():
    """
    测试 RK4 求解简谐振子时，短时间内的能量守恒性
    """
    dt = 0.05
    Y = np.array([1.0, 0.0]) # x=1, v=0
    E_initial = calc_energy(Y)
    
    t = 0.0
    # 演化 20 个周期左右
    for _ in range(2500):
        Y = rk4_step(harmonic_oscillator_deriv, Y, t, dt)
        t += dt
        
    E_final = calc_energy(Y)
    
    # RK4 虽然不是辛算法，但在步长较小时，误差增长极慢
    assert np.isclose(E_initial, E_final, atol=1e-4), f"RK4 能量误差过大: E_init={E_initial}, E_final={E_final}"
