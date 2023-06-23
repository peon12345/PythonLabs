import pygame
import Colors
import random
pygame.init()

w = 800
h = 800
screen = pygame.display.set_mode((w,h))


balloons_img = pygame.image.load("Labs/res/ballons.png")
w_balloon = 40
h_balloon = 90 

ballons = []
destroyed_ballons = []


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1:
                      m_x,m_y = pygame.mouse.get_pos()
                      #for x,y in ballons:
                      for x,y in reversed(ballons):
                        if (m_x >= x and m_y >= y and
                                m_x <= x + w_balloon and m_y <= y + h_balloon ):
                             ballons.remove((x,y))
                             destroyed_ballons.append((x,y,0))

        make_ballons = random.randint(0,5)
        if make_ballons == 1:
             x = random.randint(0,w)
             y = random.randint(0,h)
             ballons.append((x,y))

        screen.fill(Colors.BLACK)
        for i in range(len(ballons)):
             x,y = ballons[i]
             y -= 1
             screen.blit(balloons_img,(x,y),(200,200,w_balloon,h_balloon))
             ballons[i] = x,y

        
        destroyed_ballons[:] = [(x,y,frame) for (x,y,frame)  in destroyed_ballons if frame < 7]

        for i in range(len(destroyed_ballons)):
            x,y,frame = destroyed_ballons[i]
            frame += 1
            y += 10

            bonus_w = 0
            x_offset = 0
            if frame == 1:
                 bonus_w += 18
                 x_offset += w_balloon + 10
            elif frame == 2:
                 bonus_w += 18
                 x_offset += w_balloon*2 + 25
            elif frame == 3:
                 bonus_w += 25
                 x_offset += w_balloon*3 + 40
            elif frame == 4:
                 bonus_w += 25
                 x_offset += w_balloon*4 + 55
            elif frame == 5:
                 bonus_w += 30
                 x_offset += w_balloon*5 + 85
            elif frame == 6:
                 bonus_w += 35
                 x_offset += w_balloon*6 + 120
            elif frame == 7:
                 bonus_w += 45
                 x_offset += w_balloon*7 + 160

            screen.blit(balloons_img,(x,y),(200+x_offset,200,w_balloon+bonus_w,h_balloon))
            destroyed_ballons[i] = x,y,frame
        

        pygame.display.update()
        pygame.time.delay(100)
