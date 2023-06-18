import pygame
import Colors
pygame.init()


offset = 5
n = 2
numbers = input().split()[:n]
w = int(numbers[0])
h = int(numbers[1])
        
screen = pygame.display.set_mode((w,h))

screen.fill(Colors.YELLOW)

pygame.draw.rect(screen, Colors.RED, pygame.Rect(offset, offset, w-offset * 2, h-offset * 2))


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)
