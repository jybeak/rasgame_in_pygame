import pygame
import random
import chicken, background, stage01_monster

from time import sleep

WHITE = (255, 255, 255)
GRAY = (128,128,128)
pad_width = 600
pad_heigth = 480
background_width = 799

def drawObject(obj,x,y):
    global gamepad
    gamepad.blit(obj,(x,y))

def runGame():
    global gamepad, clock, chicken, background1, background2
    global blue_monster, bullet

    bullet_xy = []

    backgound_color_gray = True
    background1.pos_x = 0
    background2.pos_x = background_width


    crashed = False
    while not crashed:
        gamepad.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if backgound_color_gray == True:
                        backgound_color_gray = False
                        print(backgound_color_gray)
                        print(blue_monster.pos_x)
                    else:
                        backgound_color_gray = True
                        print(backgound_color_gray)
                        print(blue_monster.pos_x)
                elif event.key == pygame.K_LCTRL:
                    bullet_x = chicken.pos_x + 80
                    bullet_y = chicken.pos_y + 25
                    bullet_xy.append([bullet_x, bullet_y])
                    print(blue_monster.pos_x)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    chicken.change_pos_y = -15
                elif event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 15
                elif event.key == pygame.K_LEFT:
                    chicken.change_pos_x = -15
                elif event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 15
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 0

        chicken.pos_x += chicken.change_pos_x
        chicken.pos_y += chicken.change_pos_y
        if chicken.pos_x < -30:
            chicken.pos_x = -30
        elif chicken.pos_x > pad_width-30:
            chicken.pos_x = pad_width-30
        if chicken.pos_y <-30:
            chicken.pos_y = -30
        elif chicken.pos_y > pad_heigth-30:
            chicken.pos_y = pad_heigth-30

        blue_monster.pos_x -= 15
        if blue_monster.pos_x <= -40:
            blue_monster.pos_x = pad_width + 30
            blue_monster.pos_y = random.randrange(0, pad_heigth)


        
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] +=15
                bullet_xy[i][0] = bxy[0]
                drawObject(bullet, bxy[0], bxy[1])
                if bxy[0] >= pad_width:
                    bullet_xy.remove(bxy)

        background1.pos_x-=2
        background2.pos_x-=2



        if background1.pos_x < -background_width:
            background1.pos_x = 0
        if background2.pos_x < 0:
            background2.pos_x = background_width

        

        drawObject(background1.image, background1.pos_x, 0)
        drawObject(background2.image, background2.pos_x, 0)
        drawObject(blue_monster.image, blue_monster.pos_x, blue_monster.pos_y)
        drawObject(chicken.image, chicken.pos_x, chicken.pos_y)
        
        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet, bx, by)


        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, chicken, background1, background2, blue_monster, bullet

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heigth))
    pygame.display.set_caption('ChickenGun')
    chicken = chicken.Chicken()
    background1 = background.Background()
    background2 = background.Background()
    blue_monster = stage01_monster.Blue_Monster()
    bullet = pygame.image.load('resources/images/bullet.png')
    clock = pygame.time.Clock()
    runGame()

initGame()

