import pygame
import Colors
import random
pygame.init()

w = 1000
h = 600
screen = pygame.display.set_mode((w,h))

horse_img = pygame.image.load("Labs/res/horse.png")
horse_img = pygame.transform.scale(horse_img, (400,400))

fence_img = pygame.image.load("Labs/res/fence.png")
fence_img = pygame.transform.scale(fence_img,(w,40))

horse_frames_rect = []

horse_frames_rect.append((150,10,130,100))
horse_frames_rect.append((280,10,130,100))
horse_frames_rect.append((20,110,130,100))
horse_frames_rect.append((150,110,130,100))
horse_frames_rect.append((280,110,130,100))
horse_frames_rect.append((20,210,130,100))
horse_frames_rect.append((150,210,130,100))
horse_frames_rect.append((280,210,130,100))

font = pygame.font.SysFont('Comic Sans MS', 40)
text_select_horse = font.render("Your horse:", False, (200, 100, 100))

font_win = pygame.font.SysFont('Comic Sans MS', 90)
text_win = font_win.render("You win!!!", False, (200, 100, 100))
text_lose = font_win.render("You lose!!!", False, (200, 100, 100))
horses = []
input_num = 0
horse_current_frame_index = 0
running = False
width_horse = 90
clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    input_num = 1
                elif event.key == pygame.K_2:
                    input_num = 2
                elif event.key == pygame.K_3:
                    input_num = 3
        
        screen.fill(Colors.YELLOW)
        
        screen.blit(text_select_horse,(0,0))
        
        if input_num == 0:
             pygame.display.update()
             pygame.time.delay(200)
             continue 
        
        text_selected_horse = font.render(""+str(input_num)+"", False, (200, 100, 100))
        screen.blit(text_selected_horse,(200,0))

        #finish
        x_finish = w-70
        pygame.draw.rect(screen,Colors.RED,(x_finish,40,40,h - 150))

        #draw fence
        screen.blit(fence_img,(0,30))
        screen.blit(fence_img,(0,150))
        screen.blit(fence_img,(0,300))
        screen.blit(fence_img,(0,450))

        #horses
        max_speed = 10
        min_speed = 1
        
        if running == False: 
            horses.append((0,50,random.randint(min_speed,max_speed)))
            horses.append((0,200,random.randint(min_speed,max_speed)))
            horses.append((0,300,random.randint(min_speed,max_speed)))
            running = True

        horse_current_frame_index += 1
        if horse_current_frame_index >= len(horse_frames_rect):
             horse_current_frame_index = 0


        horse_finish_num = 0

        for i in range(len(horses)):
             x,y,s = horses[i]
             x += s
             
             screen.blit(horse_img,(x,y),horse_frames_rect[horse_current_frame_index])
             if x + width_horse >= x_finish:
                  horse_finish_num = i+1
                  break

             change_speed = random.randint(1,100)
             if change_speed < 50:
                  s = random.randint(min_speed,max_speed)
             horses[i] = x,y,s

        if horse_finish_num != 0:
            if input_num == horse_finish_num:
                screen.blit(text_win,(w/2,h/2))
            else:
                screen.blit(text_lose,(w/2,h/2))
            pygame.display.update()    
            pygame.time.delay(4000)
            horses.clear()
            running = False
            input_num = 0
        else:
            pygame.display.update()
            clock.tick(10)
        