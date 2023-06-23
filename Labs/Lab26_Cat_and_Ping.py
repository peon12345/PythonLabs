import pygame
import Colors
pygame.init()

w = 800
h = 800

screen = pygame.display.set_mode((w,h))

cat_img = pygame.image.load("Labs/res/cat_kick.png")
cat_img = pygame.transform.scale(cat_img,(100,100))
cat_img = pygame.transform.flip(cat_img,True,False)

penguin1_img = pygame.image.load("Labs/res/ping_1.png")
penguin1_img = pygame.transform.scale(penguin1_img,(100,100))


penguin2_img = pygame.image.load("Labs/res/ping_2.png")
penguin2_img = pygame.transform.scale(penguin2_img,(100,100))

ball_img = pygame.image.load("Labs/res/ball.png")
ball_img = pygame.transform.scale(ball_img,(50,50))


x_ball = 60
y_ball = h/2

ball_points = []

ball_points.append((280,100,3))
ball_points.append((340,100,2))
ball_points.append((600,380,2))
ball_index = 0

font = pygame.font.SysFont('Comic Sans MS', 40)
text = font.render("Поймал!", False, (200, 100, 100))

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Colors.WHITE)
        screen.blit(cat_img,(10,h/2))


        if ball_index >= len(ball_points):
           screen.blit(penguin2_img,(600,h/2))
           screen.blit(text,(600,h/2 - 100))
           
        else:
           screen.blit(penguin1_img,(600,h/2))

        screen.blit(ball_img,(x_ball,y_ball))

        if ball_index < len(ball_points):
             x,y,s = ball_points[ball_index]
             if x_ball < x:
                  x_ball += s
             elif x_ball > x:
                  x_ball -= s
             
             if y_ball > y:
                  y_ball -= s
             elif y_ball < y:
                  y_ball += s

             if y_ball >= y and x_ball >= x:
                   ball_index += 1
             


        pygame.display.update()
        pygame.time.delay(50)