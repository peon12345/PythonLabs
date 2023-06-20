import pygame
import Colors
pygame.init()

w = 1200
h = 900


screen = pygame.display.set_mode((w,h))

homer_image = pygame.image.load("Labs/res/Homer_Run.png")
homer_image = pygame.transform.scale(homer_image, (75, 150))

pub_image = pygame.image.load("Labs/res/Pub.jpeg")
pub_image = pygame.transform.scale(pub_image, (250, 250))

cong_image = pygame.image.load("Labs/res/Congratulations.png")
cong_image = pygame.transform.scale(cong_image, (w, h))


x_move = 0
y_move = 0
step = 20

x_hero_pos = 0
y_hero_pos = 0

image_is_flipped = False

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LEFT:
                      if image_is_flipped == False:
                        image_is_flipped = True
                        homer_image = pygame.transform.flip(homer_image, True, False)
                      x_move = step * -1
                 elif event.key == pygame.K_UP:
                      y_move = step * -1
                 elif event.key == pygame.K_RIGHT:
                      if image_is_flipped:
                        image_is_flipped = False
                        homer_image = pygame.transform.flip(homer_image, True, False)
                      x_move = step
                 elif event.key == pygame.K_DOWN:
                      y_move = step

            elif event.type == pygame.KEYUP:
                 if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    x_move = 0
                 elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0

        screen.fill(Colors.BLACK)

        if y_hero_pos >= h - pub_image.get_height() and x_hero_pos >= w - pub_image.get_width():
            screen.blit(cong_image,(0,0))
        else:   
            screen.blit(homer_image,(x_hero_pos,y_hero_pos))
            screen.blit(pub_image,(w - pub_image.get_width(),h - pub_image.get_height()))
        
            if x_hero_pos + x_move + homer_image.get_width() < w and x_hero_pos + x_move > 0:
                x_hero_pos += x_move
            if y_hero_pos + y_move + homer_image.get_height() < h and y_hero_pos + y_move > 0:
                y_hero_pos += y_move



        


        pygame.display.update()
        pygame.time.delay(20)