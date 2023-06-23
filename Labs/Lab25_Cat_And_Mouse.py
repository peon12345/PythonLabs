import pygame
import Colors
import random
from math import atan2, degrees, pi
pygame.init()

w = 1000
h = 600
screen = pygame.display.set_mode((w,h))


cat_img = pygame.image.load("Labs/res/Cat.png")
cat_img = pygame.transform.scale(cat_img, (50, 50))

mouse_img = pygame.image.load("Labs/res/mouse.png")
mouse_img = pygame.transform.scale(mouse_img, (35, 35))

cake_img = pygame.image.load("Labs/res/piece_of_cake.png")
cake_img = pygame.transform.scale(cake_img, (50, 50))

w_wall = 10

walls = []


def legal_move(x_move,y_move,w_object,h_object):
    result = next(((x,y,w,h) for (x,y,w,h) in walls if x_move + w_object  >= x and y_move + h_object >= y and
                                ( x_move <= x + w ) and (  y_move <= y +h) ), None)
    
    if x_move < 0 or x_move >= w:
         return False
    
    if y_move < 0 or y_move >= h:
         return False 

    return result == None

def check_collision(x,y,w_object,h_object):
     if x + w_object  >= x_cake and y + h_object >= y_cake and ( x <= x_cake + cake_img.get_width() ) and (  y <= y_cake + cake_img.get_height()):
                                
                                quit()

     if x + w_object  >= x_cat and y + h_object >= y_cat and ( x <= x_cat + w_cat ) and (  y <= y_cat + h_cat):
                                
                                quit()       



x_cake = 550
y_cake = 60


x_mouse = 200
y_mouse = 240

x_mouse_move = 0
y_mouse_move = 0
mouse_width = 20
mouse_height = 20
mouse_angle = 0


x_cat = 500
y_cat = 130
x_cat_move = 1
y_cat_move = 1
w_cat = 40
h_cat = 40
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP :
                    if legal_move(x_mouse,y_mouse-1,mouse_width,mouse_height):
                         y_mouse_move = -5
                    
                 elif event.key == pygame.K_DOWN:
                      if legal_move(x_mouse,y_mouse+1,mouse_width,mouse_height):
                           y_mouse_move = 5
                      
                 elif event.key == pygame.K_LEFT:
                      if legal_move(x_mouse - 1 , y_mouse,mouse_width,mouse_height):
                           x_mouse_move = -5
                      
                 elif event.key == pygame.K_RIGHT:
                      if legal_move(x_mouse + 1, y_mouse,mouse_width,mouse_height):
                           x_mouse_move = 5
                            
        
        if legal_move(x_mouse + x_mouse_move,y_mouse,mouse_width,mouse_height) == False:
             x_mouse_move = 0

        if legal_move(x_mouse,y_mouse + y_mouse_move,mouse_width,mouse_height) == False:
             y_mouse_move = 0     
             
        x_mouse += x_mouse_move
        y_mouse += y_mouse_move

        

        x_cat_change_move = random.randint(1,50)
        if x_cat_change_move < 3:
             x_cat_move = random.randint(-5,5) 

        y_cat_change_move =  random.randint(1,50)
        if y_cat_change_move < 3:
             y_cat_move = random.randint(-5,5)       

        if legal_move(x_cat + x_cat_move,y_cat , w_cat,h_cat) == False:
             x_cat_move *= -1

        if legal_move(x_cat,y_cat + y_cat_move,w_cat,h_cat) == False:
             y_cat_move *= -1

        x_cat += x_cat_move
        y_cat += y_cat_move

        screen.fill(Colors.YELLOW)
        pygame.draw.rect(screen,Colors.BLACK,(0,0,w,w_wall))
        walls.append((0,0,w,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(0,25,75,w_wall))
        walls.append((0,25,75,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(125,0,w_wall,210))
        walls.append((125,0,w_wall,210))
        pygame.draw.rect(screen,Colors.BLACK,(125,210,200,w_wall))
        walls.append((125,210,200,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(320,50,w_wall,170))
        walls.append((320,50,w_wall,170))
        pygame.draw.rect(screen,Colors.BLACK,(75,25,w_wall,185))
        walls.append((75,25,w_wall,185))
        pygame.draw.rect(screen,Colors.BLACK,(20,200,65,w_wall))
        walls.append((20,200,65,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(20,200,w_wall,250))
        walls.append((20,200,w_wall,250))
        pygame.draw.rect(screen,Colors.BLACK,(20,450,w,w_wall))
        walls.append((20,450,w,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(75,280,200,w_wall))
        walls.append((75,280,200,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(270,280,w_wall,110))
        walls.append((270,280,w_wall,110))
        pygame.draw.rect(screen,Colors.BLACK,(75,280,w_wall,100))
        walls.append((75,280,w_wall,100))
        pygame.draw.rect(screen,Colors.BLACK,(75,380,200,w_wall))
        walls.append((75,380,200,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(400,380,200,w_wall))
        walls.append((400,380,200,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(400,0,w_wall,380))
        walls.append((400,0,w_wall,380))
        pygame.draw.rect(screen,Colors.BLACK,(400,200,500,w_wall))
        walls.append((400,200,500,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(900,200,w_wall,180))
        walls.append((900,200,w_wall,180))
        pygame.draw.rect(screen,Colors.BLACK,(700,200,w_wall,180))
        walls.append((700,200,w_wall,180))
        pygame.draw.rect(screen,Colors.BLACK,(900,100,w_wall,100))
        walls.append((900,100,w_wall,100))
        pygame.draw.rect(screen,Colors.BLACK,(800,100,100,w_wall))
        walls.append((800,100,100,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(600,100,100,w_wall))
        walls.append((600,100,100,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(600,50,w_wall,50))
        walls.append((600,50,w_wall,50))
        pygame.draw.rect(screen,Colors.BLACK,(500,100,100,w_wall))
        walls.append((500,100,100,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(400,50,200,w_wall))
        walls.append((400,50,200,w_wall))
        pygame.draw.rect(screen,Colors.BLACK,(w-w_wall,0,w_wall,h))
        walls.append((w-w_wall,0,w_wall,h))

        x2 = x_mouse + x_mouse_move 
        y2 = y_mouse + y_mouse_move 

        xDiff = x2 - x_mouse
        yDiff = y2 - y_mouse
        v = degrees(atan2(xDiff, yDiff))
        mouse_img_rotated = pygame.transform.rotate(mouse_img, v)

        check_collision(x_mouse,y_mouse,mouse_width,mouse_height)

        screen.blit(mouse_img_rotated,(x_mouse,y_mouse))
        screen.blit(cat_img,(x_cat,y_cat))
        screen.blit(cake_img,(x_cake,y_cake))

        pygame.display.update()
        clock.tick(60)