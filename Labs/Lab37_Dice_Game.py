import pygame
import Colors
import random
pygame.init()

screen = pygame.display.set_mode((500,500))

dice_values_img = pygame.image.load("Labs/res/dice.jpg")
dice_values_img = pygame.transform.scale(dice_values_img,(400,400))

dice_rects = []
dice_rects.append((40,40,100,100))
dice_rects.append((150,40,100,100))
dice_rects.append((260,40,100,100))
dice_rects.append((40,150,100,100))
dice_rects.append((150,150,100,100))
dice_rects.append((260,260,100,100))

balance = 100
input_str_num = ""
font = pygame.font.SysFont('Comic Sans MS', 40)
point = 0
input_value = 0
wait_point_input = False



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        screen.fill(Colors.BLACK)
        if wait_point_input:
            text_enter_point = font.render("Balance "+str(balance)+" Enter point:"+input_str_num+"", False, (200, 100, 100))
            screen.blit(text_enter_point,(0,0))
        else:
            text_enter = font.render("Enter your number:"+input_str_num+"", False, (200, 100, 100))
            screen.blit(text_enter,(0,0))

        pygame.display.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                input_str_num += "1"
            elif event.key == pygame.K_2:
                input_str_num += "2"
            elif event.key == pygame.K_3:
                input_str_num += "3"
            elif event.key == pygame.K_4:
                input_str_num += "4"
            elif event.key == pygame.K_5:
                input_str_num += "5"
            elif event.key == pygame.K_6:
                input_str_num += "6"
            elif event.key == pygame.K_7:
                input_str_num += "7"
            elif event.key == pygame.K_8:
                input_str_num += "8"
            elif event.key == pygame.K_9:
                input_str_num += "9"
            elif event.key == pygame.K_9:
                input_str_num += "0"

        if event.type != pygame.KEYDOWN:
                pygame.time.delay(30)
                continue
        else:
            if event.key != pygame.K_RETURN:
                pygame.time.delay(30)
                continue
        

        
        if wait_point_input:
            point = int(input_str_num)
            if point > balance or point == 0:
                input_str_num = ""
                point  = 0
                continue
        else:
            input_value = int(input_str_num)
            if input_value > 12:
                input_str_num = ""
                input_value = 0
                continue
            else:
                wait_point_input = True
                input_str_num = ""
                continue

    
        value1 = random.randint(1,6)
        value2 = random.randint(1,6)
        result = value1 + value2
        screen.blit(dice_values_img,(0,100),dice_rects[value1-1])
        screen.blit(dice_values_img,(100,100),dice_rects[value2-1])

        if result == input_value:
            #win * 4
            balance += point * 4
            text = font.render("You win "+str(point*4)+" points", False, (200, 100, 100))
            screen.blit(text, (0,200))
        elif result < 7 and input_value < 7:
            #win
            balance += point
            text = font.render("You win "+str(point)+" points", False, (200, 100, 100))
            screen.blit(text, (0,200))
        elif result > 7 and input_value > 7:
            #win
            balance += point
            text = font.render("You win "+str(point)+" points", False, (200, 100, 100))
            screen.blit(text, (0,200))
        else:
            balance -= point
            text = font.render("You lose "+str(point)+" points", False, (200, 100, 100))
            screen.blit(text, (0,200))

        input_str_num = ""
        wait_point_input = False
        pygame.display.update()
        pygame.time.delay(3000)