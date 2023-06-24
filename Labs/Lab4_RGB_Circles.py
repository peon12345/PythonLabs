import pygame
import Colors
pygame.init()

print("Enter width and number of circles: ")

n = 2
numbers = input().split()[:n]
screen = pygame.display.set_mode((600,600))

width_circ = int(numbers[0])
n_circ = int(numbers[1])

rgb = [Colors.BLUE,Colors.GREEN,Colors.RED]

for i in range(n_circ):
    pygame.draw.circle(screen, rgb[i%3], (300,300), width_circ * (n_circ - i) )


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)
