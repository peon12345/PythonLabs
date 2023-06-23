import pygame
import Colors
import random
pygame.init()


w = 600
h = 600
screen = pygame.display.set_mode((w,h))

n_bananas = random.randint(10,40)

close_banana_image = pygame.image.load("Labs/res/banan.png")
open_banana_image = pygame.image.load("Labs/res/banana_2.png")

close_banana_image = pygame.transform.scale(close_banana_image, (50, 50))
open_banana_image = pygame.transform.scale(open_banana_image, (50, 50))

close_bananas_bounding_rects = []
open_bananas_pos = []

for i in range(n_bananas):
     x = random.randint(0,w)
     y = random.randint(0,h)
     close_bananas_bounding_rects.append((x,y,close_banana_image.get_width(),close_banana_image.get_height()))


def draw_bananas():
     screen.fill(Colors.BLACK)

     for i in range(len(close_bananas_bounding_rects)):
          x,y,w,h = close_bananas_bounding_rects[i]
          screen.blit(close_banana_image,(x,y))
          x += random.randint(-2,2)
          close_bananas_bounding_rects[i] = x,y,w,h


     for x,y in open_bananas_pos:
          screen.blit(open_banana_image,(x,y))

clock = pygame.time.Clock()
while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                      m_x,m_y = pygame.mouse.get_pos()
                      index_erase = -1
                      for i in range(len(close_bananas_bounding_rects)):
                           x,y,w,h = close_bananas_bounding_rects[i]
                           #находится ли точка в rect
                           if (m_x >= x and m_y >= y and
                               m_x <= x + w and m_y <= y + h ):
                                open_bananas_pos.append((x + w/4,y + h/4))
                                index_erase = i
                      if index_erase >= 0:
                           close_bananas_bounding_rects.pop(index_erase)

                      
                           
                              
        draw_bananas()         
        pygame.display.update()
        clock.tick(30)