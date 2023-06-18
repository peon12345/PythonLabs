import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((600,600))
square_size = 50

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.WHITE)

        pygame.draw.rect(screen,Colors.YELLOW,(300 - square_size/2,300 - square_size/2,square_size,square_size))
        square_size += 40

        if square_size > 640:
             quit()

        pygame.display.update()
        pygame.time.delay(1000)