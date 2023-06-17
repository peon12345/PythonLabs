from Point import Point


class Line:
    def __init__(self, p1, p2, width=5):
        self._p1 = p1
        self._p2 = p2
        self._width = width

    @property
    def points(self):
        return self._p1, self._p2

    @property
    def p1(self):
        return self._p1

    @property
    def p2(self):
        return self._p2

    @property
    def width(self):
        return self._width

    @p1.setter
    def p1(self, point):
        self._p1 = point

    @p2.setter
    def p2(self, point):
        self._p2 = point

    @width.setter
    def width(self, width):
        self._width = width

    # def set_points(self, p1, p2):
    #     self._p1 = p1
    #     self._p2 = p2
