from numpy import array, arange, sin, cos, power, pi, floor, ceil, min, max
from scipy.optimize import minimize_scalar
from solution2 import solve
from manim import *


config.frame_rate = 30
config.pixel_height = 720
config.pixel_width = 1280


class Phase_Space(Scene):
    def __init__(self, start_angle, b, g, l, m, T, a1, a2):
        super().__init__()

        self.Pendulum_Point = 5.6 * LEFT + 2.7 * UP
        self.Phase_Scale = 0.9

        self.T = T

        self.continuous_angles, self.continuous_speeds = solve(
            start_angle, b, g, l, m, T, a1, a2
        )

    def construct(self):
        t = ValueTracker(0)

        ### Axes

        delta = 0.001
        points = np.arange(0, self.T, delta)

        x_values = np.array([self.continuous_angles(x) for x in points])
        y_values = np.array([self.continuous_speeds(x) for x in points])

        x_min = min((-1.5, x_values.min()))
        x_max = max((1.5, x_values.max()))

        y_min = min((-1.5, y_values.min()))
        y_max = max((1.5, y_values.max()))

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

        def phase(t):
            return (
                t * self.Phase_Scale,
                self.continuous_speeds(t) * self.Phase_Scale,
            )

        point = always_redraw(
            lambda: Dot(
                axes.coords_to_point(*phase(t.get_value())), radius=0.07, z_index=2
            ).set_color(BLUE)
        )
        trace1 = TracedPath(
            point.get_center,
            dissipating_time=self.T,
            stroke_opacity=[1, 1],
            stroke_color=YELLOW,
            stroke_width=3,
            z_index=1,
        )
        self.play(Write(labels))

        ### Pendulum

        def pend(t):
            angle = self.continuous_angles(t)
            return array(
                (
                    sin(angle),
                    -cos(angle),
                    0,
                )
            )

        dashed_line = DashedLine(
            self.Pendulum_Point,
            self.Pendulum_Point + DOWN,
        ).set_color(GRAY)
        mass = always_redraw(
            lambda: Dot(
                pend(t.get_value()) + self.Pendulum_Point, radius=0.1
            ).set_color(BLUE)
        )
        line = always_redraw(
            lambda: Line(self.Pendulum_Point, pend(t.get_value()) + self.Pendulum_Point)
        )
        trace2 = TracedPath(
            mass.get_center,
            dissipating_time=0.3,
            stroke_opacity=[0, 1],
            stroke_color="#FF8C00",
            stroke_width=10,
            z_index=1,
        )

        ### Angle

        def theta(x):
            if x >= 0:
                return Angle(
                    dashed_line,
                    line,
                    radius=0.5,
                    quadrant=(1, 1),
                    stroke_width=4,
                    other_angle=False,
                    color=YELLOW,
                )
            else:
                return Angle(
                    dashed_line,
                    line,
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

        angle_phi = always_redraw(lambda: theta(self.continuous_angles(t.get_value())))
        label_phi = always_redraw(
            lambda: MathTex("\\theta", color=YELLOW, z_index=1)
            .scale(label_scale(self.continuous_angles(t.get_value())))
            .next_to(angle_phi, DOWN)
        )

        ### launch

        self.add(trace1)

        self.play(
            AnimationGroup(
                Create(dashed_line),
                Create(line),
                Create(angle_phi),
                Write(label_phi),
                DrawBorderThenFill(mass),
                FadeIn(point),
                lag_ratio=0.1,
                run_time=1,
            )
        )

        self.add(trace2)

        self.wait()

        self.play(t.animate.set_value(self.T), run_time=self.T, rate_func=linear)
