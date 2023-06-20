import pygame
import Colors
import random
pygame.init()

w = 600
h = 600

screen = pygame.display.set_mode((w,h))
banana_image = pygame.image.load("Labs/res/banana_2.png")
banana_image = pygame.transform.scale(banana_image, (50, 50))

bananas = []

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        screen.fill(Colors.BLACK)
        draw_banana_rand = random.randint(0, 10)

        if draw_banana_rand < 2: 
            x = random.randint(0, w)
            y = random.randint(50, 200)
            bananas.append((x,y))

        for i in range(len(bananas)):
             x,y = bananas[i]
             screen.blit(banana_image,(x,y))
             y += 15
             x += random.randint(-5, 5)
             bananas[i] = x,y
        

        pygame.display.update()
        pygame.time.delay(100)