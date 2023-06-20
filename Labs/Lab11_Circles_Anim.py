import pygame
import Colors
import random

pygame.init()

w_screen = 600
h_screen = 600

screen = pygame.display.set_mode((w_screen,h_screen))


blue_circle_x = random.randint(0, w_screen)
blue_circle_y = random.randint(0, h_screen)

yellow_circle_x = random.randint(0, w_screen)
yellow_circle_y = random.randint(0, h_screen)

max_distance = 20

yellow_step = 5

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.WHITE)
        pygame.draw.circle(screen,Colors.BLUE,(blue_circle_x,blue_circle_y), 15)
        pygame.draw.circle(screen,Colors.YELLOW,(yellow_circle_x,yellow_circle_y), 15)

        #yellow move
        if yellow_circle_x > blue_circle_x + yellow_step:
             yellow_circle_x -= yellow_step
        elif yellow_circle_x < blue_circle_x - yellow_step:
             yellow_circle_x += yellow_step

        if yellow_circle_y > blue_circle_y + yellow_step:
             yellow_circle_y -= yellow_step
        elif yellow_circle_y < blue_circle_y - yellow_step:
             yellow_circle_y += yellow_step

        if abs(yellow_circle_y - blue_circle_y) <= 50 or abs(yellow_circle_x - blue_circle_x) <= 50:
             blue_circle_x = random.randint(0, w_screen)
             blue_circle_y = random.randint(0, h_screen)

        pygame.display.update()
        pygame.time.delay(50)