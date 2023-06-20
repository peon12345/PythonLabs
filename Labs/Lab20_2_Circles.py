import pygame
import Colors
import random

pygame.init()

w = 150
h = 150
screen = pygame.display.set_mode((w,h))

x1 = random.randint(0,w)
y1 = random.randint(0,h)

x2 = random.randint(0,w)
y2 = random.randint(0,h)

r_circle = 10
x_move_c1 = random.randint(-5,5)
y_move_c1 = random.randint(-5,5)
speed_c1 = 10

x_move_c2 = random.randint(-5,5)
y_move_c2 = random.randint(-5,5)
speed_c2 = 10

c1_color = Colors.BLUE
c2_color = Colors.RED

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Colors.BLACK)

        pygame.draw.circle(screen,c1_color,(x1,y1),r_circle)
        pygame.draw.circle(screen,c2_color,(x2,y2),r_circle)
    
        x1 += x_move_c1
        y1 += y_move_c1
        x2 += x_move_c2
        y2 += y_move_c2

        #check collision circles and walls
        if abs(x1 - x2) < r_circle*2 and abs(y1 - y2) < r_circle*2:
             x_move_c1 *= -1
             y_move_c1 *= -1
             x_move_c2 *= -1
             y_move_c2 *= -1
             c1_color,c2_color = c2_color,c1_color

        
        
        if x1 <= 0 or x1 >= w:
             x_move_c1 *= -1
        if x2 <= 0 or x2 >= w:
             x_move_c2 *= -1
        if y1 <= 0 or y1 >= h:
             y_move_c1 *= -1
        if y2 <= 0 or y2 >= h:
             y_move_c2 *= -1             
             


        pygame.display.update()
        pygame.time.delay(50)