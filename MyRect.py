

class Rect:
    def __init__(self,p1, p2, p3, p4):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4

    @property
    def points(self):
        return self._p1, self._p2, self._p3, self._p4


