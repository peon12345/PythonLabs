import pygame
import Colors
pygame.init()


game_over_image = pygame.image.load("Labs/res/Game_Over.jpg")

screen = pygame.display.set_mode((game_over_image.get_width(),game_over_image.get_height()))


x = game_over_image.get_width() * -1
y = 0
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit() 
        
        screen.fill(Colors.BLACK)
        screen.blit(game_over_image,(x,y))

        if x < 0:
             x+= 20

        pygame.display.update()
        pygame.time.delay(50)