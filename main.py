from MathPlot import MathPlot
import pygame
from Lines import Lines
from Line import Line
from Point import Point

pygame.init()

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))

    plot = MathPlot(screen.get_width()-100, screen.get_height()-100)
    

    my_func = Lines()

    my_func.add_line(Line(Point(1,1), Point(2,2)))
    my_func.add_line(Line(Point(0,0), Point(2,10)))
    my_func.add_line(Line(Point(10,10), Point(20,20)))

    plot.set_lines_func(my_func)
    
    plot.draw(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()

