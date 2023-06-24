import pygame
pygame.init()

print("Enter width cube and hue")

w = 300
h = 300
screen = pygame.display.set_mode((w,h))

arg_size = 2
numbers = input().split()[:arg_size]

size_cube = int(numbers[0])
hue = int(numbers[1])


color_75_hue = pygame.Color(255, 255, 255)
hsv = color_75_hue.hsva
color_100_hue = pygame.Color(255, 255, 255)
hsv2 = color_100_hue.hsva
color_50_hue = pygame.Color(255, 255, 255)
hsv3 = color_50_hue.hsva
 
color_75_hue.hsva = (hue, hsv[1] + 100, hsv[2] - 25, hsv[3])
color_100_hue.hsva = (hue, hsv2[1] + 100, hsv2[2], hsv[3])
color_50_hue.hsva = (hue, hsv3[1] + 100, hsv3[2] - 50, hsv[3])

x_front = w/2 - size_cube/2
y_front = h/2

pygame.draw.rect(screen,color_75_hue,(x_front,y_front,size_cube,size_cube))

pygame.draw.polygon(screen,color_100_hue,((x_front,y_front),
                                          (x_front+size_cube/2,y_front-size_cube/2),
                                          (x_front+size_cube*1.5,y_front-size_cube/2),
                                          (x_front+size_cube,y_front)) )

pygame.draw.polygon(screen,color_50_hue,((x_front+size_cube,y_front),
                                         (x_front+size_cube*1.5,y_front-size_cube/2),
                                         (x_front + size_cube*1.5,y_front + size_cube/2),
                                         (x_front+size_cube,y_front+size_cube) ))


while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()
        pygame.time.delay(1000)
