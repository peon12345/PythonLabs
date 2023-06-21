import pygame
import Colors
import random

pygame.init()

screen = pygame.display.set_mode((900,600))

number = random.randint(0,9)

n_try = 0
font = pygame.font.SysFont('Comic Sans MS', 40)
text = font.render("Угадай число от 0-9 за 3 попытки", False, (200, 100, 100))
screen.blit(text,(0,0))

y_text = 0
game_end = False
while True:
        input_num = -1 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_0:
                      input_num = 0
                 elif event.key == pygame.K_1:
                      input_num = 1
                 elif event.key == pygame.K_2:
                    input_num = 2
                 elif event.key == pygame.K_3:
                      input_num = 3
                 elif event.key == pygame.K_4:
                      input_num = 4
                 elif event.key == pygame.K_5:
                      input_num = 5
                 elif event.key == pygame.K_6:
                      input_num = 6
                 elif event.key == pygame.K_7:
                      input_num = 7
                 elif event.key == pygame.K_8:
                      input_num = 8
                 elif event.key == pygame.K_9:
                      input_num = 9
                 else:
                      continue
        if input_num > 0:
            if game_end:
                continue

            if number == input_num:
                text = font.render("Угадал!", False, (200, 100, 100))
                game_end = True
            elif number < input_num:
                n_try += 1
                text = font.render("Загаданное число МЕНЬШЕ. Осталось попыток: "+str(3 - n_try)+"", False, (200, 100, 100))
            elif number > input_num:
                n_try += 1
                text = font.render("Загаданное число БОЛЬШЕ. Осталось попыток: "+str(3 - n_try)+"", False, (200, 100, 100))
             
            y_text += 50
            if n_try >= 3:
                text = font.render("Проиграл! Число: "+str(number)+"", False, (200, 100, 100))
                screen.blit(text,(0,y_text))
            else:
                screen.blit(text,(0,y_text))


        pygame.display.update()
        pygame.time.delay(400)