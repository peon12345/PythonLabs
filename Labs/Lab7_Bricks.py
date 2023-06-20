import pygame
import Colors
import math
pygame.init()


w = 300
h = 200

screen = pygame.display.set_mode((w,h))
screen.fill(Colors.WHITE)


h_brick = 15
w_brick = 30
interval = 2

n_bricks_col = math.ceil(w/w_brick)
n_bricks_row = math.ceil(h/h_brick)

y = 0
for row in range(n_bricks_row):
    x_offset = 0

    if row % 2 != 0:
         x_offset -= 15

    for col in range(n_bricks_col):
        pygame.draw.rect(screen,Colors.RED,(x_offset,y,w_brick,h_brick))
        x_offset += w_brick + interval
    y += h_brick + interval

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)

