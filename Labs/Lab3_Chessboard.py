import pygame
import Colors

pygame.init()

print("Enter size side and rect num: ")

n = 2
numbers = input().split()[:n]

size_side = int(numbers[0])
n_rect = int(numbers[1])

black_rect_draw_turn = (n_rect % 2 != 0)

square_side = size_side / n_rect

screen = pygame.display.set_mode((size_side,size_side))

x_pos = 0
y_pos = 0

for row in range(n_rect):
    x_pos = 0
    for col in range(n_rect):
        color = Colors.WHITE
        if black_rect_draw_turn:
            color = Colors.BLACK
        pygame.draw.rect(screen, color, pygame.Rect(x_pos, y_pos, square_side, square_side))
        black_rect_draw_turn = not black_rect_draw_turn
        x_pos += square_side
    if n_rect % 2 == 0:
        black_rect_draw_turn = not black_rect_draw_turn

    y_pos += square_side




while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)

