import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((600,600))



x_rect = 0
y_rect = 0

x_mouse_offset = 0
y_mouse_offset = 0

is_captured = False
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                      m_x,m_y = pygame.mouse.get_pos()
                      if m_x >= x_rect and m_x < x_rect + 100:
                            if m_y >= y_rect and m_y < y_rect + 100:
                                is_captured = True
                                x_mouse_offset = m_x - x_rect
                                y_mouse_offset = m_y - y_rect
                 
            elif event.type == pygame.MOUSEBUTTONUP:
                 is_captured = False
            elif event.type == pygame.MOUSEMOTION:
                 if is_captured:
                      x_rect,y_rect = pygame.mouse.get_pos()
                      x_rect -= x_mouse_offset
                      y_rect -= y_mouse_offset
  
        screen.fill(Colors.WHITE)
        pygame.draw.rect(screen,Colors.GREEN,(x_rect,y_rect,100,100))

        pygame.display.update()
        pygame.time.delay(50)