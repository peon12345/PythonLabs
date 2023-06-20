import pygame
import Colors
import random
pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w ,h))

car_img = pygame.image.load("Labs/res/Car.png")
car_img = pygame.transform.scale(car_img, (200, 100))

tree_img = pygame.image.load("Labs/res/Tree_1.png")
tree_img = pygame.transform.scale(tree_img, (50, 100))

wheel = pygame.image.load("Labs/res/wheel.png")
wheel = pygame.transform.scale(wheel, (37, 37))

road_img = pygame.image.load("Labs/res/Road.png")
#road_img = pygame.transform.scale(road_img, (500, h))

angle = 0
x_wheel_1 = 0
y_wheel_1 = 0



trees = []


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.BLACK)

        screen.blit(road_img,(-100,h/2 - 90))
        screen.blit(car_img,(w/2,h/2))
        angle += 10
        rotated_wheel = pygame.transform.rotate(wheel, angle) 
        
        
        screen.blit(rotated_wheel, (rotated_wheel.get_rect(center=wheel.get_rect(topleft= (w/2+30, h/2+50) ).center).topleft))
        screen.blit(rotated_wheel, (rotated_wheel.get_rect(center=wheel.get_rect(topleft= (w/2+140, h/2+50) ).center).topleft))
        



        make_tree = random.randint(0,100)
        if make_tree < 4:
             y = random.randint(200,220)
             trees.append((-50,y))

        for i in range(len(trees)):
             x,y = trees[i]
             if x < w:
                x += 1
                trees[i] = x,y
                screen.blit(tree_img,(x,y))
             else:
                trees.remove(x)  

        pygame.display.update()
        pygame.time.delay(100)