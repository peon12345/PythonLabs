import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((800,800))




while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)