from numpy import array, arange, sin, cos, power, pi, floor, ceil, min, max
from scipy.optimize import minimize_scalar
from solution3 import solve
from manim import *


config.frame_rate = 30
config.pixel_height = 720
config.pixel_width = 1280


class Phase_Space(Scene):
    def __init__(self, a1, a2, g, l1, l2, m1, m2, T):
        super().__init__()

        self.Pendulum_Point = 5.6 * LEFT + 2.7 * UP
        self.Phase_Scale = 0.9

        self.T = T

        (
            self.continuous_angles1,
            self.continuous_speeds1,
            self.continuous_angles2,
            self.continuous_speeds2,
        ) = solve(a1, a2, g, l1, l2, m1, m2, T)

    def construct(self):
        t = ValueTracker(0)

        ### Axes

        delta = 0.001
        points = np.arange(0, self.T, delta)

        x1_values = np.array([self.continuous_angles1(x) for x in points])
        y1_values = np.array([self.continuous_speeds1(x) for x in points])

        x2_values = np.array([self.continuous_angles2(x) for x in points])
        y2_values = np.array([self.continuous_speeds2(x) for x in points])

        x_min = min((-1.5, x1_values.min(), x2_values.min()))
        x_max = max((1.5, x1_values.max(), x2_values.max()))

        y_min = min((-1.5, y1_values.min(), y2_values.min()))
        y_max = max((1.5, y1_values.max(), y1_values.max()))

        axes = Axes(
            x_range=[x_min, x_max],
            y_range=[y_min, y_max],
            x_length=14.2 * self.Phase_Scale,
            y_length=8 * self.Phase_Scale,
            axis_config={
                "include_tip": True,
                # "color": GREY,
                "stroke_width": 2,
                "font_size": 24,
                "tick_size": 0.07,
                "longer_tick_multiple": 1.5,
                "line_to_number_buff": 0.15,
                "decimal_number_config": {
                    # "color": ORANGE,
                    "num_decimal_places": 0
                },
            },
            x_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": arange(ceil(x_min), floor(x_max) + 1, 1),
                "numbers_with_elongated_ticks": [-1, 1],
            },
            y_axis_config={
                "tip_width": 0.15,
                "tip_height": 0.15,
                "numbers_to_include": arange(ceil(y_min), floor(y_max) + 1, 1),
                "tick_size": 0.08,
                "font_size": 25,
                "numbers_with_elongated_ticks": [-1, 1],
            },
        )
        x_lab = axes.get_x_axis_label("\\theta", direction=UP, buff=0.2)
        y_lab = axes.get_y_axis_label("\\theta'", direction=RIGHT, buff=0.2)
        labels = VGroup(x_lab.scale(1), y_lab.scale(1))

        self.play(Write(axes, run_time=1), lag_ratio=0.2)

        ### Phase space

        def phase1(t):
            return (
                self.continuous_angles1(t) * self.Phase_Scale,
                self.continuous_speeds1(t) * self.Phase_Scale,
            )

        point1 = always_redraw(
            lambda: Dot(
                axes.coords_to_point(*phase1(t.get_value())), radius=0.07, z_index=2
            ).set_color(GREEN)
        )
        trace21 = TracedPath(
            point1.get_center,
            dissipating_time=self.T,
            stroke_opacity=[1, 1],
            stroke_color=GREEN_A,
            stroke_width=3,
            z_index=1,
        )

        def phase2(t):
            return (
                self.continuous_angles2(t) * self.Phase_Scale,
                self.continuous_speeds2(t) * self.Phase_Scale,
            )

        point2 = always_redraw(
            lambda: Dot(
                axes.coords_to_point(*phase2(t.get_value())), radius=0.07, z_index=2
            ).set_color(RED)
        )
        trace22 = TracedPath(
            point2.get_center,
            dissipating_time=self.T,
            stroke_opacity=[1, 1],
            stroke_color=YELLOW,
            stroke_width=3,
            z_index=1,
        )

        self.play(Write(labels))

        ### Pendulum

        def pend1(t):
            angle = self.continuous_angles1(t)
            return array(
                (
                    sin(angle),
                    -cos(angle),
                    0,
                )
            )

        def pend2(t):
            angle = self.continuous_angles2(t)
            return array(
                (
                    sin(angle),
                    -cos(angle),
                    0,
                )
            )

        dashed_line = DashedLine(
            self.Pendulum_Point,
            self.Pendulum_Point + 2 * DOWN,
        ).set_color(GRAY)
        mass1 = always_redraw(
            lambda: Dot(
                pend1(t.get_value()) + self.Pendulum_Point, radius=0.1
            ).set_color(GREEN)
        )
        line1 = always_redraw(lambda: Line(self.Pendulum_Point, mass1.get_center()))
        mass2 = always_redraw(
            lambda: Dot(
                mass1.get_center() + pend2(t.get_value()), radius=0.1
            ).set_color(RED)
        )
        line2 = always_redraw(lambda: Line(mass1.get_center(), mass2.get_center()))
        trace11 = TracedPath(
            mass1.get_center,
            dissipating_time=0.3,
            stroke_opacity=[0, 1],
            stroke_color=GREEN_A,
            stroke_width=10,
            z_index=1,
        )
        trace12 = TracedPath(
            mass2.get_center,
            dissipating_time=0.3,
            stroke_opacity=[0, 1],
            stroke_color="#FF8C00",
            stroke_width=10,
            z_index=1,
        )

        ### Angle

        def theta1(x):
            if x > 0:
                return Angle(
                    dashed_line,
                    line1,
                    radius=0.5,
                    quadrant=(1, 1),
                    stroke_width=4,
                    other_angle=False,
                    color=YELLOW,
                )
            else:
                return Angle(
                    dashed_line,
                    line1,
                    radius=0.5,
                    quadrant=(1, 1),
                    stroke_width=4,
                    other_angle=True,
                    color=YELLOW,
                )

        def theta2(x):
            if x > 0:
                return Angle(
                    line1,
                    line2,
                    radius=0.5,
                    quadrant=(1, 1),
                    stroke_width=4,
                    other_angle=False,
                    color=YELLOW,
                )
            else:
                return Angle(
                    line1,
                    line2,
                    radius=0.5,
                    quadrant=(1, 1),
                    stroke_width=4,
                    other_angle=True,
                    color=YELLOW,
                )

        def label_scale(x):
            if x >= pi:
                while x > pi:
                    x = x - 2 * pi
            elif x < -pi:
                while x < -pi:
                    x = x + 2 * pi

            x = abs(x)

            if x > 1:
                return 1
            else:
                return power(x, 1 / 3)

        angle_phi1 = always_redraw(
            lambda: theta1(self.continuous_angles1(t.get_value()))
        )
        label_phi1 = always_redraw(
            lambda: MathTex("\\theta_1", color=YELLOW, z_index=1)
            .scale(label_scale(self.continuous_angles2(t.get_value())))
            .next_to(angle_phi1, DOWN)
        )
        angle_phi2 = always_redraw(
            lambda: theta2(self.continuous_angles1(t.get_value()))
        )
        label_phi2 = always_redraw(
            lambda: MathTex("\\theta_2", color=YELLOW, z_index=1)
            .scale(label_scale(self.continuous_angles2(t.get_value())))
            .next_to(angle_phi2, DOWN)
        )

        ### launch

        self.add(trace11, trace12)

        self.play(
            AnimationGroup(
                Create(dashed_line),
                Create(line1, line2),
                Create(angle_phi1, angle_phi2),
                Write(label_phi1, label_phi2),
                DrawBorderThenFill(mass1, mass2),
                FadeIn(point1, point2),
                lag_ratio=0.1,
                run_time=1,
            )
        )

        self.add(trace21, trace22)

        self.wait()

        self.play(t.animate.set_value(self.T), run_time=self.T, rate_func=linear)
