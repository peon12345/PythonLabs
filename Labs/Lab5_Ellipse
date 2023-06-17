import pygame 
import Colors
pygame.init()


print("Enter count ellipse: ")
n_ellipse = int(input())


screen = pygame.display.set_mode((300,300))
screen.fill(Colors.BLACK)


x_interval = 300 / n_ellipse
xy_draw_offset = 0
for i in range(n_ellipse):
     pygame.draw.ellipse(screen, Colors.WHITE, (xy_draw_offset / 2, 0, 300 - xy_draw_offset, 300),1)
     pygame.draw.ellipse(screen, Colors.WHITE, (0, xy_draw_offset / 2, 300 , 300- xy_draw_offset),1)
     xy_draw_offset += x_interval


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)