import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((600,600))

circles = []
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 m_x,m_y = pygame.mouse.get_pos()
                 circles.append((m_x,m_y,10))
         
        screen.fill(Colors.WHITE)
        for i in range(len(circles)):
            x,y,r = circles[i]
            pygame.draw.circle(screen,Colors.RED,(x,y),r)
            circles[i] = x,y,r+1

            if r > 700:
                 quit()

    
             
        pygame.display.update()
        clock.tick(60)
