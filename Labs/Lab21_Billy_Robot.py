import pygame
import Colors
pygame.init()

w = 200
h = 200
screen = pygame.display.set_mode((w,h))


robot_image = pygame.image.load("Labs/res/Billy_Robot.png")
robot_image = pygame.transform.scale(robot_image, (250, 250))

x = 8
y = 10

font = pygame.font.SysFont('Comic Sans MS', 30)
text_select_direct = font.render('Select move direct:', False, (200, 100, 100))

text_W =  font.render("W - up", False, (200, 100, 100))
text_S = font.render("S - down", False, (200, 100, 100))
text_A = font.render("A - left", False, (200, 100, 100))
text_D = font.render("D - right", False, (200, 100, 100))

x = 8
y = 10
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_w:
                 if y - 1 > 0:
                  y -= 1
             elif event.key == pygame.K_s:
                  if y + 1 < h:
                    y += 1
             elif event.key == pygame.K_a:
                 if x - 1 > 0:
                  x -= 1
             elif event.key == pygame.K_d:
                 if x + 1 < w:
                  x += 1

        screen.fill(Colors.BLACK)
        screen.blit(text_select_direct,(0,0))
        screen.blit(text_W,(0,20))
        screen.blit(text_S,(0,40))
        screen.blit(text_A,(0,60))
        screen.blit(text_D,(0,80))

        text_pos = font.render("x: "+str(x)+" y: "+str(y)+" ", False, (200, 100, 100))
        screen.blit(text_pos,(0,100))

        pygame.display.update()
        pygame.time.delay(50)