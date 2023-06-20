import pygame
import Colors
import random

pygame.init()
w = 600
h = 600
screen = pygame.display.set_mode((600,600))

banana_image = pygame.image.load("Labs/res/banan.png")
banana_image = pygame.transform.scale(banana_image, (50, 50))
n_bananas = random.randint(10, 100)

for i in range(n_bananas):
     x = random.randint(0, w)
     y = random.randint(0, h)
     screen.blit(banana_image,(x,y))


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        pygame.display.update()
        pygame.time.delay(1000)