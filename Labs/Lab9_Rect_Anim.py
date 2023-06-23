import pygame
import Colors

screen = pygame.display.set_mode((600,600))
h_rect = 50
w_rect = 150

x = 0
y = 600 - h_rect

clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.WHITE)
        pygame.draw.rect(screen,Colors.GREEN,(x,y,w_rect,h_rect))
        x+=5
        y-=5

        if y < -100:
             quit()

        pygame.display.update()
        #pygame.time.delay(200)
        clock.tick(60)