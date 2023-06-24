import pygame
import Colors
pygame.init()


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rect:
    def __init__(self,p1, p2, p3, p4):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._p4 = p4

    def points(self):
        return self._p1, self._p2, self._p3, self._p4
    

def bezier_curve(rect):
    t = 0.0
    step = 75

    points_result = []

    for i in map(lambda x: x/100.0, range(0, 105, 5)):
        t += 1 / step
        ps = rect.points()
        x = (1.0-i)**3*ps[0].x + 3*(1.0-i)**2*i*ps[1].x + 3*(1.0-i)*i**2*ps[2].x + i**3*ps[3].x
        y = (1.0-i)**3*ps[0].y + 3*(1.0-i)**2*i*ps[1].y + 3*(1.0-i)*i**2*ps[2].y + i**3*ps[3].y

        points_result.append((x,y))
    return points_result


font = pygame.font.SysFont('Comic Sans MS', 20)

w = 800
h = 800

padding_len = 50
line_width = 3


screen = pygame.display.set_mode((w,h))

w = w - padding_len
h = h - padding_len

x_screen = padding_len
y_screen = padding_len

screen.fill(Colors.WHITE)
line_num_x = 12 #кол -во нужных делений на отрезке
one_step = w//line_num_x # это интервал между 0 1, 
y_line_offset = 7
#draw math plot
pygame.draw.line(screen,Colors.BLACK,(x_screen,h//2),(w,h//2),line_width)
x_pos_vertical_line = one_step * y_line_offset + one_step
pygame.draw.line(screen,Colors.BLACK,(x_pos_vertical_line,h),(x_pos_vertical_line,y_screen),line_width)

#draw line mark

line_offset = 5

x_num_value = -y_line_offset
for i in range(1,line_num_x):
    pygame.draw.line(screen,Colors.BLACK,(i*one_step,h//2+line_offset),(i*one_step,h//2-line_offset),line_width-1)
    #draw numbers
    text_num = font.render(str(x_num_value), False, (0, 0, 0))
    x_num_value += 1
    screen.blit(text_num,(i*one_step + 3,h//2+line_offset+1))


#find pos draw y nums
x_center_plot = x_pos_vertical_line
y_center_plot = h//2

number_down = (h - y_center_plot) // one_step
number_up = (y_center_plot - y_screen) // one_step
total = number_down + number_up

y_pos_mark = y_center_plot + number_down * one_step

pygame.draw.circle(screen,Colors.BLACK,(x_center_plot,y_center_plot),5)

y_num_value = -number_down
for i in range(1,total):
    pygame.draw.line(screen,Colors.BLACK,(x_pos_vertical_line + line_offset,y_pos_mark),(x_pos_vertical_line- line_offset,y_pos_mark ),line_width-1)
    #draw numbers
    text_num = font.render(str(y_num_value), False, (0, 0, 0))
    
    if y_num_value != 0: #ноль уже нарисован
        screen.blit(text_num,(x_pos_vertical_line - line_offset - line_width - 3,y_pos_mark)) 
    y_num_value += 1
    y_pos_mark -= one_step  

#arrow and x y text
x_arrow = w - 10
pygame.draw.line(screen,Colors.BLACK,(x_arrow,h//2+10),(w,h//2),line_width)
pygame.draw.line(screen,Colors.BLACK,(x_arrow,h//2-10),(w,h//2),line_width)


pygame.draw.line(screen,Colors.BLACK,(x_pos_vertical_line,y_screen),(x_pos_vertical_line+ 10,y_screen+10),line_width)
pygame.draw.line(screen,Colors.BLACK,(x_pos_vertical_line,y_screen),(x_pos_vertical_line- 10, y_screen+10 ),line_width)
text_x = font.render("x", False, (0, 0, 0))
text_y = font.render("y", False, (0, 0, 0))
screen.blit(text_x,(w,h//2+10))
screen.blit(text_y,(x_pos_vertical_line+10,y_screen))

#draw lines 
def convert_pos(x,y):
     x_left_value = -y_line_offset
     y_down_value = -number_down

     converted_x = one_step * abs(x_left_value - x) + one_step
     converted_y = h - one_step * abs(y_down_value - y)
     if converted_y == 0:
          converted_y = y_center_plot

     return converted_x,converted_y

pygame.draw.line(screen,Colors.BLACK,(convert_pos(-6,-1)),(convert_pos(-2,0)),line_width)

rect = Rect(Point(-2,0),Point(-0.9,0),Point(0,0.9),Point(0,2) )
points = bezier_curve(rect)

for i in range(len(points)):
    x,y = points[i]
    x,y = convert_pos(x,y)
    points[i] = x,y

pygame.draw.lines(screen, Colors.BLACK, False, points, line_width)

rect = Rect(Point(0,2),Point(2,1.75),Point(2,0.25),Point(2,0))

points = bezier_curve(rect)

for i in range(len(points)):
    x,y = points[i]
    x,y = convert_pos(x,y)
    points[i] = x,y

pygame.draw.lines(screen, Colors.BLACK, False, points, line_width)

pygame.draw.line(screen,Colors.BLACK,(convert_pos(2,0)),(convert_pos(3,-1)),line_width)

dot_line_interval = 15
#-6 -1  3 -1  dotted line
x1 , y1 = convert_pos(-6,-1)
x2 , y2 = convert_pos(3,-1)
n = x2 - x1

for i in range(1,n,dot_line_interval):
    pygame.draw.line(screen,Colors.BLACK,(x1 + i-5,y2),(x1 + i,y2),line_width)

# -6 2  -6 -1 dotted line

x2 ,y2 = convert_pos(-6,2)
n = y1 - y2  

for i in range(1,n,dot_line_interval):
    pygame.draw.line(screen,Colors.BLACK,(x1 ,y1 - i-5),(x1,y1 - i),line_width)

#dotted line 
x1 , y1 = convert_pos(0,2)
n = x1 - x2

for i in range(1,n,dot_line_interval):
    pygame.draw.line(screen,Colors.BLACK,(x2+i + 5,y2),(x2 + i,y2),line_width)

#dotted line 
x1,y1 = convert_pos(3,-1)
x2,y2 = convert_pos(3,0)

n = y1 - y2
for i in range(1,n,dot_line_interval):
    pygame.draw.line(screen,Colors.BLACK,(x1 ,y1 - i-5),(x1,y1 - i),line_width)

#dotted line
x1,y1 = convert_pos(-2,0)
x2,y2 = convert_pos(-2,2)

n = y1 - y2
for i in range(1,n,dot_line_interval):
    pygame.draw.line(screen,Colors.BLACK,(x1 ,y1 - i-5),(x1,y1 - i),line_width)

#arrow line 1
x1,y1 = convert_pos(-0.5,0.75)
pygame.draw.line(screen,Colors.BLACK,(x2,y2),(x1,y1),line_width)
pygame.draw.line(screen,Colors.BLACK,(x1,y1),(convert_pos(-0.70,1.1)),line_width)
pygame.draw.line(screen,Colors.BLACK,(x1,y1),(convert_pos(-0.9,0.9)),line_width)
text_R = font.render("R", False, (0, 0, 0))
screen.blit(text_R,(convert_pos(-1,1.5)))


#arrow line 2
x1,y1 = convert_pos(1.7,1)
pygame.draw.line(screen,Colors.BLACK,(convert_pos(0,0)),(x1,y1),line_width)
pygame.draw.line(screen,Colors.BLACK,(convert_pos(1.5,0.8)),(x1,y1),line_width)
pygame.draw.line(screen,Colors.BLACK,(convert_pos(1.4,0.9)),(x1,y1),line_width)


screen.blit(text_R,(convert_pos(0.7,0.75)))

pygame.display.update()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.time.delay(1000)

