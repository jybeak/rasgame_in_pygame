import pygame
import random
import chicken, background, stage01_monster, ui

from time import sleep

WHITE = (255, 255, 255)
pad_width = 600
pad_heigth = 480
background_width = 799

background_SW = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def check_collision_chicken_monsters():
    if collide(chicken, blue_monster):
        blue_monster.pos_x = pad_width + 30
        blue_monster.pos_y = random.randrange(0, pad_heigth - 50)
        chicken.health -= 10
    if collide(chicken, red_monster):
        red_monster.pos_x = pad_width + 30
        red_monster.pos_y = random.randrange(0, pad_heigth - 50)
        chicken.health -= 10

def drawObject(obj,x,y):     #그리기
    gamepad.blit(obj,(x,y))
    
def drawScore(count): #점수표시
    font = pygame.font.SysFont(None, 40)
    text = font.render('Score:' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (pad_width*3/7, 0))
    
def runGame():     #시작
    global gamepad, clock, chicken, background1, background2
    global blue_monster, red_monster, bullet, ui, background_SW

    bullet_xy = []

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
                    bullet_pos_x = chicken.pos_x + 80
                    bullet_pos_y = chicken.pos_y + 25
                    bullet_xy.append([bullet_pos_x,bullet_pos_y])
                    if background_SW == 0:
                        background_SW = 1
                    else:
                        background_SW =0
                elif event.key == pygame.K_0:
                    if chicken.skillgauge > 194:
                        chicken.skillgauge = 0
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
            for i,bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                if bxy[0] > blue_monster.pos_x:
                    if bxy[1]>blue_monster.pos_y and bxy[1] < blue_monster.pos_y + 49:
                        bullet_xy.remove(bxy)
                        blue_monster.pos_x = pad_width + 30
                        blue_monster.pos_y = random.randrange(0, pad_heigth - 50)
                        ui.score +=10
                        chicken.skillgauge +=10
                if bxy[0] > red_monster.pos_x:
                    if bxy[1]>red_monster.pos_y and bxy[1] < red_monster.pos_y + 49:
                        bullet_xy.remove(bxy)
                        red_monster.pos_x = pad_width + 30
                        red_monster.pos_y = random.randrange(0, pad_heigth - 50)
                        ui.score += 20
                        chicken.skillgauge += 20

                if bxy[0] >= pad_width*3:
                    bullet_xy.remove(bxy)




        

        drawObject(background1.image, background1.pos_x, 0)
        drawObject(background2.image, background2.pos_x, 0)
        drawObject(blue_monster.image, blue_monster.pos_x, blue_monster.pos_y)
        drawObject(red_monster.image, red_monster.pos_x, red_monster.pos_y)
        drawObject(chicken.image, chicken.pos_x, chicken.pos_y)



        if len(bullet_xy) != 0:
            for bx,by in bullet_xy:
                drawObject(bullet,bx,by)



        drawObject(ui.backgroundstatewindow_image, 0, 0)
        if background_SW == 0:
            drawObject(ui.backgroundstatesun_image, 0, 0)
        elif background_SW == 1:
            drawObject(ui.backgroundstatemoon_image, 0, 0)

        drawObject(ui.healthbar_image, pad_width*3/7, pad_heigth*9/10)
        drawObject(ui.skillgaugebar_imgae, pad_width * 1/18, pad_heigth * 9 / 10)
        for HP in range(chicken.health):
            drawObject(ui.health_image, HP + pad_width*3/7 + 3  , pad_heigth*9/10 + 3)
        for SG in range(chicken.skillgauge):
            drawObject(ui.skillgauge_imgae, SG + pad_width*1/18 + 3  , pad_heigth*9/10 + 3)
        drawScore(ui.score)


        check_collision_chicken_monsters()

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
