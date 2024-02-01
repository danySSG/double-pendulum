from manim import *


class DivideFrame(Scene):
    def construct(self):
        # Создание фрейма
        frame = self.camera.frame

        # Разделение экрана на 2x2
        top_left = frame.get_corner(UL)
        top_right = frame.get_corner(UR)
        bottom_left = frame.get_corner(DL)
        bottom_right = frame.get_corner(DR)

        mid_top = frame.get_top()
        mid_left = frame.get_left()
        mid_right = frame.get_right()
        mid_bottom = frame.get_bottom()

        # Создание объектов для каждой из частей
        top_left_rect = ScreenRectangle(
            height=2, width=2, color=BLUE, fill_opacity=0.5
        ).move_to(top_left)
        top_right_rect = ScreenRectangle(
            height=2, width=2, color=RED, fill_opacity=0.5
        ).move_to(top_right)
        bottom_left_rect = ScreenRectangle(
            height=2, width=2, color=GREEN, fill_opacity=0.5
        ).move_to(bottom_left)
        bottom_right_rect = ScreenRectangle(
            height=2, width=2, color=YELLOW, fill_opacity=0.5
        ).move_to(bottom_right)

        mid_top_rect = SurroundingRectangle(
            frame, buff=0, color=ORANGE, fill_opacity=0.5
        ).move_to(mid_top)
        mid_left_rect = SurroundingRectangle(
            frame, buff=0, color=PURPLE, fill_opacity=0.5
        ).move_to(mid_left)
        mid_right_rect = SurroundingRectangle(
            frame, buff=0, color=TEAL, fill_opacity=0.5
        ).move_to(mid_right)
        mid_bottom_rect = SurroundingRectangle(
            frame, buff=0, color=PINK, fill_opacity=0.5
        ).move_to(mid_bottom)

        # Добавление объектов на сцену
        self.play(
            Create(top_left_rect),
            Create(top_right_rect),
            Create(bottom_left_rect),
            Create(bottom_right_rect),
            Create(mid_top_rect),
            Create(mid_left_rect),
            Create(mid_right_rect),
            Create(mid_bottom_rect),
        )
        self.wait(2)
