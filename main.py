from MathPlot import MathPlot
import pygame

pygame.init()

if __name__ == '__main__':
    screen = pygame.display.set_mode((800, 600))

    plot = MathPlot(screen.get_width()-100, screen.get_height()-100)
    plot.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()

