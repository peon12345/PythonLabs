import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((600,600))

x_circ = 0
y_circ = 0
circ_step = 10

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        screen.fill(Colors.WHITE)

        m_x,my = pygame.mouse.get_pos()
        if x_circ > m_x + circ_step:
             x_circ -= circ_step
        elif x_circ < m_x - circ_step:
             x_circ += circ_step

        if y_circ > my + circ_step:
             y_circ -= circ_step
        elif y_circ < my - circ_step:
             y_circ += circ_step

        pygame.draw.circle(screen,Colors.YELLOW,(x_circ,y_circ),30)

        pygame.display.update()
        pygame.time.delay(100)