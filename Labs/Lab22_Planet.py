import pygame
import Colors
import random
import math 
pygame.init()


w = 800
h = 800
screen = pygame.display.set_mode((w,h))

font = pygame.font.SysFont('Comic Sans MS', 40)
text = font.render("12 Апреля", False, (200, 100, 100))


planet_img = pygame.image.load("Labs/res/earth_sprite.png")
planet_img = pygame.transform.scale(planet_img, (600, 600))

rocket_img = pygame.image.load("Labs/res/rocket.png")
rocket_img = pygame.transform.scale(rocket_img, (50, 50))

stars = []

n_stars = 50
for i in range(n_stars):
        x = random.randint(0,w)
        y = random.randint(0,h)
        r = random.randint(1,3)
        pygame.draw.circle(screen,Colors.WHITE,(x,y),r)
        stars.append((x,y))

x_crop_planet = 0
y_crop_planet = 0
w_crop_image_planet = 120
h_crop_image_planet = 100

rocket_fly_points = []
rocket_fly_points.append((w/2,h/2,30))
rocket_fly_points.append((w/8,h/8,180))
rocket_fly_points.append((w/7,h/1.1,260))
rocket_fly_points.append((w - 100 ,h - 100,30))

len_rocket_points = len(rocket_fly_points)

x_rocket, y_rocket,angle = rocket_fly_points[0]
rocket_img_rotated = pygame.transform.rotate(rocket_img,angle)
current_index_point = 0
step_rocket = 10

rotate = False
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Colors.BLACK)

        for i in range(len(stars)):
              x,y = stars[i]
              r = random.randint(0,3)
              pygame.draw.circle(screen,Colors.WHITE,(x,y),r)


        x_crop_planet += w_crop_image_planet
        y_crop_planet += h_crop_image_planet
        if x_crop_planet >= planet_img.get_width() or y_crop_planet >= planet_img.get_height():
             x_crop_planet = 0
             y_crop_planet = 0

        screen.blit(rocket_img_rotated,(x_rocket,y_rocket))

        screen.blit(planet_img,(w/2,h/2),(x_crop_planet, y_crop_planet, w_crop_image_planet, h_crop_image_planet))

        x_target,y_target,angle = rocket_fly_points[current_index_point]

        if x_rocket != x_target and abs(x_target - x_rocket) > step_rocket:
            if x_rocket < x_target:
                  x_rocket += step_rocket
            else:
                  x_rocket -= step_rocket

        if y_rocket != y_target and abs(y_target - y_rocket) > step_rocket:
              if y_rocket < y_target:
                    y_rocket += step_rocket
              else:
                    y_rocket -= step_rocket

        if (y_rocket == y_target or abs(y_target - y_rocket) <= step_rocket) and (x_rocket == x_target or abs(x_target - x_rocket) <= step_rocket) :
              rocket_img_rotated = pygame.transform.rotate(rocket_img,angle)
              if current_index_point < len_rocket_points-1:
                    
                    current_index_point += 1
              else:
                    current_index_point = 0

        

        screen.blit(text,(0,0))
        
        pygame.display.update()
        clock.tick(10)