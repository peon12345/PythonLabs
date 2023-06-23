import pygame
import Colors
import random
pygame.init()


w = 500
h = 200
screen = pygame.display.set_mode((w,h))

magic_number_str = str(random.randint(1000,9999))
print(magic_number_str)


def restart():
    global input_num_str
    input_num_str = ""

    global magic_number_str
    magic_number_str = str(random.randint(1000,9999))


font = pygame.font.SysFont('Comic Sans MS', 60)

input_num_str = ""
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_0:
                      input_num_str += "0"
                 elif event.key == pygame.K_1:
                      input_num_str += "1"
                 elif event.key == pygame.K_2:
                    input_num_str += "2"
                 elif event.key == pygame.K_3:
                      input_num_str += "3"
                 elif event.key == pygame.K_4:
                      input_num_str += "4"
                 elif event.key == pygame.K_5:
                      input_num_str += "5"
                 elif event.key == pygame.K_6:
                      input_num_str += "6"
                 elif event.key == pygame.K_7:
                      input_num_str += "7"
                 elif event.key == pygame.K_8:
                      input_num_str += "8"
                 elif event.key == pygame.K_9:
                      input_num_str += "9"

        screen.fill(Colors.LIGHT_BLUE)
        text_num_input = font.render("Number: "+input_num_str+"", False, (200, 100, 100))
        screen.blit(text_num_input,(0,0))
                 
        cow_counter = 0
        bull_counter = 0
        if len(input_num_str) == len(magic_number_str):
            

            for i in range(len(magic_number_str)):
                 #cow
                 if magic_number_str[i] == input_num_str[i]:
                           cow_counter +=1
                 
                 if input_num_str[i] in magic_number_str:
                      bull_counter += 1
      
            
            if  cow_counter == len(magic_number_str):
                screen.fill(Colors.LIGHT_BLUE)
                text_win = font.render("You win!", False, (200, 100, 100))
                screen.blit(text_win,(0,h/2))
                pygame.display.update()
                pygame.time.delay(2000)
                restart()
                continue

            input_num_str = ""
            text_cows_bulls = font.render("Cows: "+str(cow_counter)+". Bulls: "+str(bull_counter)+" ", False, (200, 100, 100))
            screen.blit(text_cows_bulls,(0,h/2))
            pygame.display.update()
            pygame.time.delay(3000)
        else:
            pygame.display.update()
            pygame.time.delay(200)

        
        
        