import pygame
import Colors
pygame.init()


size_rhomb = int(input())

w = 155
h = 155

screen = pygame.display.set_mode((w,h))
screen.fill(Colors.YELLOW)

n_diamond_row = int(w/size_rhomb)
n_diamond_col = int(h/size_rhomb)

y = 0

for row in range(n_diamond_row):
    x = 0
    for col in range(n_diamond_col):
         pygame.draw.polygon(screen, Colors.ORANGE, ((x + size_rhomb/2, y), (size_rhomb + x, size_rhomb/2 + y), (size_rhomb/2 + x, size_rhomb + y), (x, size_rhomb/2 + y)))
         x += size_rhomb
    y += size_rhomb


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)
