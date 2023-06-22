import pygame
import Colors
pygame.init()

screen = pygame.display.set_mode((600,600))

horse_img = pygame.image.load("Labs/res/horse.png")
horse_img = pygame.transform.scale(horse_img, (400,400))
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

horses = []

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        # x = 0
        # y = 0
        # i= 0
        # for rect in horse_frames_rect:
        #     screen.blit(horse_img,(x,y),rect)
        #     y += 200
        #     i +=1
        #     if i % 3 == 0:
        #         x += 100
        #         y = 0
        
        text = font.render("Select horse 1,2,3", False, (200, 100, 100))



        pygame.display.update()
        pygame.time.delay(1000)