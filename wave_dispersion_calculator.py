import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = 9.80665  # m/s^2
MAX_ITER = 100
TOL = 1e-8

def solve_dispersion(T, d):
    """Solve linear dispersion relation for given wave period T (s) and depth d (m).
    Returns (k, L, c, cg, classification).
    """
    omega = 2.0 * np.pi / T
    omega2 = omega**2
    # Eckart approximation for initial guess
    arg = (omega2 * d / G) ** 0.75
    if arg > 700:  # avoid overflow in coth
        k0 = omega2 / G
    else:
        k0 = (omega2 / G) * np.cosh(arg) / np.sinh(arg)
    # Newton-Raphson
    k = k0
    for it in range(MAX_ITER):
        tanh_kd = np.tanh(k * d)
        sech2_kd = 1.0 - tanh_kd * tanh_kd  # sech^2 = 1 - tanh^2
        f = omega2 - G * k * tanh_kd
        df = -G * (tanh_kd + k * d * sech2_kd)
        if abs(df) < 1e-15:
            break
        k = k - f / df
        if abs(f) < TOL:
            break
    L = 2.0 * np.pi / k
    c = omega / k
    # Group velocity cg
    kd = k * d
    cg = 0.5 * c * (1.0 + 2.0 * kd / np.sinh(2.0 * kd))
    # Water depth classification
    if d / L < 0.05:
        wl_class = "Shallow Water"
    elif d / L > 0.5:
        wl_class = "Deep Water"
    else:
        wl_class = "Intermediate Water"
    return k, L, c, cg, wl_class

def compute_ursell(k, d, H):
    """Compute Ursell number and classify wave nonlinearity.
    Returns (Ur, classification).
    """
    Ur = H * (2.0 * np.pi / k)**2 / (d**3)
    if Ur < 0.01:
        cls = "Linear waves"
    elif Ur < 0.1:
        cls = "Weakly nonlinear"
    else:
        cls = "Strongly nonlinear (Stokes)"
    return Ur, cls

def generate_dispersion_curve(T_current, d):
    """Generate matplotlib figure of phase speed c vs T for given depth,
    with the current T marked.
    """
    T_vals = np.linspace(1., 30., 100)
    k_vals = np.array([solve_dispersion(t, d)[0] for t in T_vals])
    c_vals = (2. * np.pi / T_vals) / k_vals  # omega/k
    # Find current c
    k_cur, _, c_cur, _, _ = solve_dispersion(T_current, d)
    fig, ax = plt.subplots()
    ax.plot(T_vals, c_vals, 'b-', label='Dispersion curve')
    ax.plot(T_current, c_cur, 'ro', markersize=8, label=f'Current T = {T_current:.1f} s')
    ax.set_xlabel('Wave period T (s)')
    ax.set_ylabel('Phase speed c (m/s)')
    ax.set_title(f'Water depth = {d:.1f} m')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    return fig
