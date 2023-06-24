import pygame
import Colors
import math

pygame.init()

size_side = 200
n_rect = 8



square_side = size_side / n_rect

screen = pygame.display.set_mode((size_side,size_side))

def draw_chessboard():
     black_rect_draw_turn = (n_rect % 2 == 0)
     screen.fill(Colors.WHITE)
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



font = pygame.font.SysFont('Comic Sans MS', 40)
draw_chessboard()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    m_x,m_y = pygame.mouse.get_pos()
                    x_rect_index = int(m_x / square_side)
                    y_rect_index = int(m_y / square_side)
                    if x_rect_index % 2 != 0 and y_rect_index % 2 == 0:
                        text = font.render("White", False, (200, 100, 100))
                    elif x_rect_index % 2 == 0 and y_rect_index % 2 == 0:
                        text = font.render("Black", False, (200, 100, 100))
                    elif x_rect_index % 2 == 0 and y_rect_index % 2 != 0:
                        text = font.render("White", False, (200, 100, 100))
                    elif x_rect_index % 2 != 0 and y_rect_index % 2 != 0:
                        text = font.render("Black", False, (200, 100, 100))
                    draw_chessboard()
                    screen.blit(text,(0,0))


    pygame.display.update()
    pygame.time.delay(100)