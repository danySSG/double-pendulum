from numpy import sin, cos, linspace
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Константы
RELATIVE_TOLERANCE = 1e-10
ABSOLUTE_TOLERANCE = 1e-13


def solve(start_angle, b, g, l, m, T):
    """
    Решает заданную систему дифференциальных уравнений.
    """

    def dSdt(t, S):
        """
        Функция, представляющая систему дифференциальных уравнений.
        """
        x1, x2 = S  # x1 представляет положение, x2 представляет скорость
        return [x2, - (g / l) * sin(x1) - (b / (m * l)) * x2]

    S0 = (start_angle, 0)  # начальные условия: положение 'a', скорость 0

    t = linspace(0, T, T * 1000 + 1)
    sol = solve_ivp(
        dSdt,
        t_span=(0, max(t)),
        y0=S0,
        t_eval=t,
        method="DOP853",
        rtol=RELATIVE_TOLERANCE,
        atol=ABSOLUTE_TOLERANCE,
    )

    time_range = tuple(sol.t)

    return (
        interp1d(time_range, sol.y[0], kind="linear"),  # Интерполяция положения
        interp1d(time_range, sol.y[1], kind="linear"),  # Интерполяция скорости
    )
