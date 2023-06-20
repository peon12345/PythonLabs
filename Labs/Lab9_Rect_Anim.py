import pygame
import Colors


screen = pygame.display.set_mode((600,600))
h_rect = 50
w_rect = 150

x = 0
y = 600 - h_rect

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        screen.fill(Colors.WHITE)
        pygame.draw.rect(screen,Colors.GREEN,(x,y,w_rect,h_rect))
        x+=25
        y-=25

        if y < -100:
             quit()

        pygame.display.update()
        pygame.time.delay(200)