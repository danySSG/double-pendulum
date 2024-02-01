from numpy import sin, cos, linspace
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d

# Константы
RELATIVE_TOLERANCE = 1e-10
ABSOLUTE_TOLERANCE = 1e-13


def solve(a1, a2, g, l1, l2, m1, m2, T):
    """
    Решает заданную систему дифференциальных уравнений.
    """

    def dSdt(t, S):
        """
        Функция, представляющая систему дифференциальных уравнений.
        """
        x1, y1, x2, y2 = S

        # Углы отклонения
        theta1 = x1
        theta2 = x2

        # Угловые скорости
        dx1 = y1
        dy1 = (
            -g * (2 * m1 + m2) * sin(theta1)
            - m2 * g * sin(theta1 - 2 * theta2)
            - 2
            * sin(theta1 - theta2)
            * m2
            * (l2 * (y2**2) + l1 * (y1**2) * cos(theta1 - theta2))
        ) / (l1 * (2 * m1 + m2 - m2 * cos(2 * (theta1 - theta2))))

        dx2 = y2
        dy2 = (
            2
            * sin(theta1 - theta2)
            * (
                l1 * (y1**2) * (m1 + m2)
                + g * (m1 + m2) * cos(theta1)
                + l2 * (y2**2) * m2 * cos(theta1 - theta2)
            )
        ) / (l2 * (2 * m1 + m2 - m2 * cos(2 * (theta1 - theta2))))

        return [dx1, dy1, dx2, dy2]

    S0 = (a1, 0, a2, 0)  # начальные условия

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
        interp1d(
            time_range, sol.y[0], kind="linear"
        ),  # Интерполяция положения первого маятника
        interp1d(
            time_range, sol.y[1], kind="linear"
        ),  # Интерполяция скорости первого маятника
        interp1d(
            time_range, sol.y[2], kind="linear"
        ),  # Интерполяция положения второго маятника
        interp1d(
            time_range, sol.y[3], kind="linear"
        ),  # Интерполяция скорости второго маятника
    )
