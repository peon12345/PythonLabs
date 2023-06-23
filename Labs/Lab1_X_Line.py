import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((800, 600))

screen.fill(Colors.YELLOW)

pygame.draw.line(screen,Colors.BLACK, (0, 0), (800, 600), 7)
pygame.draw.line(screen,Colors.BLACK, (800, 0), (0, 600), 7)
pygame.display.update()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)
