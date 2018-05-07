import pygame
import random
import chicken, background, stage01_monster, ui

from time import sleep

WHITE = (255, 255, 255)
GRAY = (128,128,128)
pad_width = 600
pad_heigth = 480
background_width = 799

def drawObject(obj,x,y):     #그리기
    global gamepad
    gamepad.blit(obj,(x,y))

def runGame():     #시작
    global gamepad, clock, chicken, background1, background2
    global blue_monster, red_monster, bullet, ui

    bullet_xy = []

    backgound_color_gray = True


    crashed = False
    while not crashed:
        gamepad.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    chicken.change_pos_y = -15
                elif event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 15
                elif event.key == pygame.K_LEFT:
                    chicken.change_pos_x = -15
                elif event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 15
                elif event.key == pygame.K_LCTRL:
                    bullet_x = chicken.pos_x + 80
                    bullet_y = chicken.pos_y + 25
                    bullet_xy.append([bullet_x, bullet_y])
                    chicken.health -= 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 0   #키입력

        chicken.pos()
        blue_monster.pos()
        red_monster.pos()
        background1.pos()
        background2.pos()


        
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] +=15
                bullet_xy[i][0] = bxy[0]
                drawObject(bullet, bxy[0], bxy[1])
                if bxy[0] >= pad_width:
                    bullet_xy.remove(bxy)

        

        drawObject(background1.image, background1.pos_x, 0)
        drawObject(background2.image, background2.pos_x, 0)
        drawObject(blue_monster.image, blue_monster.pos_x, blue_monster.pos_y)
        drawObject(red_monster.image, red_monster.pos_x, red_monster.pos_y)
        drawObject(chicken.image, chicken.pos_x, chicken.pos_y)
        drawObject(ui.healthbar_image, pad_width*1/3, pad_heigth*9/10)
        for HP in range(chicken.health):
            drawObject(ui.health_image, HP + pad_width*1/3 + 3  , pad_heigth*9/10 + 3)


        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet, bx, by)


        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, chicken, background1, background2, blue_monster, red_monster, bullet, ui

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heigth))
    pygame.display.set_caption('ChickenGun')
    chicken = chicken.Chicken()
    background1 = background.Background1()
    background2 = background.Background2()
    blue_monster = stage01_monster.Blue_Monster()
    red_monster = stage01_monster.Red_Monster()
    ui = ui.Ui()
    bullet = pygame.image.load('resources/images/bullet.png')
    clock = pygame.time.Clock()
    runGame()

initGame()