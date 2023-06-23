import pygame
import Colors
import random
pygame.init()

words = []

words.append("hello")
words.append("love")
words.append("apple")
words.append("orange")
words.append("death metal")
words.append("gun")
words.append("uncle")


w = 500
h = 200
screen = pygame.display.set_mode((w,h))

letters = []
magic_word = words[random.randint(0,len(words) - 1)]

print(magic_word)


for i in range(len(magic_word)):
     letters.append('_')
     
points = 15
def restart():
    global points
    points = 15

    global magic_word
    magic_word = words[random.randint(0,len(words) - 1)]

    global letters
    letters.clear()

    for i in range(len(magic_word)):
        letters.append('_')


font = pygame.font.SysFont('Comic Sans MS', 60)


while True:
        input_letter = ''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                 input_letter = event.unicode

        if input_letter != '':
            index = 0
            found = False
            while index != -1:
                index = magic_word.find(input_letter,index,len(magic_word))
                if index >= 0:
                    letters[index] = input_letter
                    index +=1
                    found = True

            if found == False:
                 points -= 1
                 if points <= 0:
                    screen.fill(Colors.LIGHT_BLUE)
                    text_lose = font.render("You lose! Word: "+magic_word+"", False, (200, 100, 100))
                    screen.blit(text_lose,(0,h/2))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    restart()
                    continue
            
            if '_' not in letters:
                screen.fill(Colors.LIGHT_BLUE)
                text_win = font.render("You win! Word: "+magic_word+"", False, (200, 100, 100))
                screen.blit(text_win,(0,h/2))
                pygame.display.update()
                pygame.time.delay(2000)
                restart()
                continue

        screen.fill(Colors.LIGHT_BLUE)
        text = font.render(' '.join(letters), False, (200, 100, 100))
        text_points = font.render("Points: "+str(points)+"", False, (200, 100, 100))
        screen.blit(text,(0,h/2))
        screen.blit(text_points,(0,h/2+50))


        pygame.display.update()
        pygame.time.delay(200)