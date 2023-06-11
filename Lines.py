from MyLine import Line
from MyRect import Rect
from MyPoint import Point
from collections import deque


class Lines:

    def __init__(self):
        self._lines = deque()

    def __iter__(self):
        return self._lines.__iter__()

    def add_line(self, line):
        self._lines.append(line)

    def add_bezier_curve(self, rect):
        t = 0.0
        step = 25

        prev_point = None
        while t <= 1 + 1 / step:
            t += 1 / step
            point = self.__point_on_curve(t, rect)

            if prev_point is None:
                prev_point = point
            else:
                self._lines.append(Line(prev_point, point))
                prev_point = None

    @staticmethod
    def __point_on_curve(self, t, rect):

        t_diff = 1 - t
        t_diff_cube = t_diff * t_diff * t_diff
        t_cube = t * t * t
        ps = rect.points()

        x = t_diff_cube * ps[0].x + 3 * t * t_diff * t_diff * ps[1].x + 3 * t * t * t_diff * ps[2].x + t_cube * ps[3].x,
        y = t_diff_cube * ps[0].y + 3 * t * t_diff * t_diff * ps[1].y + 3 * t * t * t_diff * ps[2].y + t_cube * ps[3].y
        return Point(x, y)

















