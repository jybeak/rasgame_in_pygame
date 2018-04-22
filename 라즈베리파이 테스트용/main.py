import pygame
import RPi.GPIO as GPIO
import random
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN)

WHITE = (255, 255, 255)
GRAY = (128,128,128)
pad_width = 600
pad_heigth = 480
background_width = 799

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def back(background,x,y):
    global gamepad
    gamepad.blit(background,(x,y))

def player(x,y):
    global gamepad, chicken
    gamepad.blit(chicken, (x,y))

def runGame():
    global gamepad, clock, chicken, background1, background2
    global monster, bullet

    bullet_xy = []



    x = pad_heigth *0.05
    y = pad_heigth * 0.8
    x_change = 0
    y_change = 0
    backgound_color_gray = True
    background1_x = 0
    background2_x = background_width 

    monster_x = pad_width
    monster_y = random.randrange(0,pad_heigth)

    button01_control = True




    crashed = False
    while not crashed:
        if GPIO.input(17) == 1 and button01_control == True:
            print(1)
            button01_control = False
            bullet_x = x + 80
            bullet_y = y + 25
            bullet_xy.append([bullet_x, bullet_y])
        elif GPIO.input(17) == 0 and button01_control == False:
            print(0)
            button01_control = True
        if GPIO.input(27) == 1 and backgound_color_gray == True:
            backgound_color_gray = False
            print(1)
            time.sleep(0.05)
        elif GPIO.input(27) == 1 and backgound_color_gray == False:
            backgound_color_gray = True
            print(2)
            time.sleep(0.05)

        for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_SPACE:
            #        if backgound_color_gray == True:
            #            backgound_color_gray = False
            #            print(backgound_color_gray)
            #            print(monster_x)
            #        else:
            #            backgound_color_gray = True
            #            print(backgound_color_gray)
            #            print(monster_x)
                #elif event.key == pygame.K_LCTRL:
                #    bullet_x = x + 80
                #    bullet_y = y + 25
                #    bullet_xy.append([bullet_x, bullet_y])
                #    print(monster_x)

            if event.type == pygame.QUIT:
                crashed = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -15
                elif event.key == pygame.K_DOWN:
                    y_change = 15
                elif event.key == pygame.K_LEFT:
                    x_change = -15
                elif event.key == pygame.K_RIGHT:
                    x_change = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        y += y_change
        x += x_change

        if x < -30:
            x = -30
        elif x > pad_width-30:
            x = pad_width-30
        if y <-30:
            y = -30
        elif y > pad_heigth-30:
            y = pad_heigth-30

        if (backgound_color_gray == True):
            gamepad.fill(WHITE)
        else:
            gamepad.fill(GRAY)
        
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] +=15
                bullet_xy[i][0] = bxy[0]
                drawObject(bullet, bxy[0], bxy[1])
                if bxy[0] >= pad_width:
                    bullet_xy.remove(bxy)

        background1_x-=2
        background2_x-=2



        monster_x -=15
        if monster_x<=-40:
            monster_x = pad_width+30
            monster_y = random.randrange(0, pad_heigth)

        if background1_x == -background_width:
            background1_x = background_width
        if background2_x == -background_width:
            background2_x = background_width

        

        #back(background1, background1_x, 0)
        #back(background2, background2_x, 0)
        drawObject(monster, monster_x, monster_y)
        #if len(bullet_xy) != 0:
        #    for bx,by in bullet_xy:
        #        drawObject(bullet, bx, by)
        player(x,y)


        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, chicken, background1, background2, monster, bullet

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heigth))
    pygame.display.set_caption('ChickenGun')
    chicken = pygame.image.load('resources/images/chicken.png')
    background1 = pygame.image.load('resources/images/background.png')
    background2 = background1.copy()
    monster = pygame.image.load('resources/images/blue_monster.png')
    bullet = pygame.image.load('resources/images/bullet.png')
    clock = pygame.time.Clock()
    runGame()

initGame()

