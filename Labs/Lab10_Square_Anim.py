import pygame
import Colors
pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w,h))
square_size = 50
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.WHITE)

        pygame.draw.rect(screen,Colors.YELLOW,(w/2 - square_size/2,h/2 - square_size/2,square_size,square_size))
        square_size += 4

        if square_size > 640:
             quit()

        pygame.display.update()
        clock.tick(60)