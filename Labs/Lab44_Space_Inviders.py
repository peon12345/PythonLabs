import pygame
import Colors
import random
pygame.init() 

w = 900
h = 900
screen = pygame.display.set_mode((w,h))

rocket_img = pygame.image.load("Labs/res/rocket_attack.png")
rocket_img = pygame.transform.scale(rocket_img,(70,70))

enemy_img = pygame.image.load("Labs/res/ufo_enemy.png")
enemy_img = pygame.transform.scale(enemy_img,(70,70))

enemies = []

x = 0
y = 0
x_interval = w/10
for r in range(3):
    y += 100
    x = 0
    for c in range(5):
        enemies.append((x,y))
        x += x_interval

x_rocket = w/2
y_rocket = h - rocket_img.get_height() + 10
rocket_step = 40

x_rocket_move = 0

x_enemy_step = 10
y_enemy_step = 1


enemy_bullets = []
rocket_bullets = []
bullet_step = 15

clock = pygame.time.Clock()
while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                     x_rocket_move = -rocket_step
                elif event.key == pygame.K_RIGHT:
                     x_rocket_move = rocket_step
                elif event.key == pygame.K_UP:
                     if len(rocket_bullets) < 3:
                        rocket_bullets.append((x_rocket+rocket_img.get_width()/2,y_rocket))
            

            elif event.type == pygame.KEYUP:
                    x_rocket_move = 0

        screen.fill(Colors.BLACK)

        x_rocket += x_rocket_move
        screen.blit(rocket_img,(x_rocket,y_rocket))

        
        len_enemies = len(enemies)
        for i in range(len_enemies):
             x,y = enemies[i]
             screen.blit(enemy_img,(x,y))

             #shot
             shot = random.randint(0,100*len(enemies))
             if shot < 10:
                  enemy_bullets.append((x,y))

             #move
             if x >= w- enemy_img.get_width():
                  if x_enemy_step > 0:
                    x_enemy_step = -x_enemy_step 
             elif x <= 0:
                    x_enemy_step = abs(x_enemy_step)
             
             if y >= h:
                  quit() #enemies out of battle

             x += x_enemy_step
             y += y_enemy_step
             enemies[i] = x,y

        #bullets check collision
        enemy_bullets[:] = [(x,y) for (x,y)  in enemy_bullets if y < h]
        for i in range(len(enemy_bullets)):
             x,y = enemy_bullets[i]
             if x >= x_rocket and y >= y_rocket and x <= x_rocket + rocket_img.get_width() and y < y_rocket + rocket_img.get_height():
                  quit() #dead
             y += bullet_step
             enemy_bullets[i] = x,y
             pygame.draw.rect(screen,Colors.RED,(x,y,5,15))

        rocket_bullets[:] = [(x,y) for (x,y)  in rocket_bullets if y > 0]

        for i in range(len(rocket_bullets)):
             x_bullet,y_bullet = rocket_bullets[i]
             enemies[:] = [(x,y) for (x,y)  in enemies if x_bullet <= x or y_bullet <= y or x_bullet >= x + enemy_img.get_width() or y_bullet > y + enemy_img.get_height()]
             new_len_enemies = len(enemies)
             if new_len_enemies == 0:
                  quit()
                  
             if len_enemies != new_len_enemies:
                  #enemy dead,destroy bullet
                  y_bullet = -1
                  rocket_bullets[i] = x_bullet,y_bullet
                  len_enemies = new_len_enemies
             else:
                  y_bullet -= bullet_step
                  rocket_bullets[i] = x_bullet,y_bullet
                  pygame.draw.rect(screen,Colors.BLUE,(x_bullet,y_bullet,5,15))


        pygame.display.update()
        clock.tick(25)