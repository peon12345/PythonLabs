import pygame.draw

from Drawable import Drawable
from Lines import Lines
from Line import Line
from Point import Point
import Colors
from copy import copy
from collections import namedtuple


class MathPlot(Drawable):
    __numPos = namedtuple("numPos", ["num", "pos"])
   
    def __init__(self, x_len, y_len, x_offset=0, y_offset=0):

        self.__lines_plot = Lines()
        self.__lines_func = Lines()

        self._x_len = x_len
        self._y_len = y_len

        # x line
        p1_x_line = Point(0, y_len / 2 - x_offset)
        p2_x_line = Point(x_len, y_len / 2 - x_offset)

        # x text pos
        self._point_draw_text_x = Point(p2_x_line.x, p2_x_line.y + 10)

        # y line
        p1_y_line = Point(x_len/2 - y_offset, 0)
        p2_y_line = Point(x_len/2 - y_offset, y_len)

        # y text pos
        self._point_draw_text_y = Point(p1_y_line.x + 10, p1_y_line.y)

        self.__lines_plot.add_line(Line(p1_x_line, p2_x_line))
        self.__lines_plot.add_line(Line(p1_y_line, p2_y_line))

        # x arrow
        p_x_arrow = Point(p2_x_line.x, p2_x_line.y)

        p1_x_line_arrow_up = Point(p_x_arrow.x - 10,   p_x_arrow.y + 10)
        p1_x_line_arrow_down = Point(p_x_arrow.x - 10, p_x_arrow.y - 10)
        self.__lines_plot.add_line(Line(p1_x_line_arrow_up, p_x_arrow))
        self.__lines_plot.add_line(Line(p1_x_line_arrow_down, p_x_arrow))

        # y arrow
        p_y_arrow = Point(p1_y_line.x, p1_y_line.y)
        p1_y_line_arrow_left = Point(p_y_arrow.x-10, p_y_arrow.y + 10)
        p1_y_line_arrow_right = Point(p_y_arrow.x + 10, p_y_arrow.y + 10)
        self.__lines_plot.add_line(Line(p1_y_line_arrow_left, p_y_arrow))
        self.__lines_plot.add_line(Line(p1_y_line_arrow_right, p_y_arrow))

        self.__make_markup_lines(Line(p1_x_line, p2_x_line), Line(p1_y_line, p2_y_line))


    def __make_markup_lines(self, line_x, line_y):
        interval = 10

        right_line_x = copy(line_y)
        right_line_x.p1 = Point(line_y.p1.x, line_x.p1.y - 5)
        right_line_x.p2 = Point(line_y.p1.x, line_x.p1.y + 5)

        while right_line_x.p1.x < line_x.p2.x - interval:
            right_line_x.p1 = Point(right_line_x.p1.x + interval, right_line_x.p1.y)
            right_line_x.p2 = Point(right_line_x.p2.x + interval, right_line_x.p2.y)
            self.__lines_plot.add_line(Line(right_line_x.p1, right_line_x.p2, 2))
            #self._numsPos.append()

        left_line_x = copy(line_y)
        left_line_x.p1 = Point(line_y.p1.x, line_x.p1.y - 5)
        left_line_x.p2 = Point(line_y.p1.x, line_x.p1.y + 5)

        while left_line_x.p1.x > 0:
            left_line_x.p1 = Point(left_line_x.p1.x - interval, left_line_x.p1.y)
            left_line_x.p2 = Point(left_line_x.p2.x - interval, left_line_x.p2.y)
            self.__lines_plot.add_line(Line(left_line_x.p1, left_line_x.p2, 2))

        down_line_y = copy(line_y)

        down_line_y.p1 = Point(down_line_y.p1.x - 5, line_x.p1.y)
        down_line_y.p2 = Point(down_line_y.p2.x + 5, line_x.p1.y)

        while down_line_y.p2.y < line_y.p2.y:
            down_line_y.p1 = Point(down_line_y.p1.x, down_line_y.p1.y + interval)
            down_line_y.p2 = Point(down_line_y.p2.x, down_line_y.p2.y + interval)
            self.__lines_plot.add_line(Line(down_line_y.p1, down_line_y.p2, 2))

        up_line_y = copy(line_y)
        up_line_y.p1 = Point(up_line_y.p1.x - 5, line_x.p1.y)
        up_line_y.p2 = Point(up_line_y.p2.x + 5, line_x.p1.y)

        while up_line_y.p1.y > interval:
            up_line_y.p1 = Point(up_line_y.p1.x,up_line_y.p1.y - interval)
            up_line_y.p2 = Point(up_line_y.p2.x,up_line_y.p2.y - interval)
            self.__lines_plot.add_line(Line(up_line_y.p1, up_line_y.p2, 2))

    def set_lines_func(self, lines):
        self.__lines_func = copy(lines)

    def draw(self, screen):
        # screen offset value
        s_offset = 50

        screen.fill(Colors.WHITE)

        font = pygame.font.SysFont(None, 34)
        img_x = font.render('x', True, Colors.BLACK)
        screen.blit(img_x, (self._point_draw_text_x.x+s_offset, self._point_draw_text_x.y+s_offset))

        img_y = font.render('y', True, Colors.BLACK)
        screen.blit(img_y, (self._point_draw_text_y.x + s_offset, self._point_draw_text_y.y+s_offset))

        for line in self.__lines_plot:
            pygame.draw.line(screen, Colors.BLACK, (line.p1.x+s_offset, line.p1.y+s_offset),
                             (line.p2.x+s_offset, line.p2.y+s_offset), line.width)

        for line in self.__lines_func:
            print("draw func line")
            pygame.draw.line(screen, Colors.BLACK, (line.p1.x+s_offset, line.p1.y+s_offset),
                             (line.p2.x+s_offset, line.p2.y+s_offset), line.width)
