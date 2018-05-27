import pygame
import random
import time
import chicken, background, stage01_monster, ui, bullet_01, bullet


WHITE = (255, 255, 255)
pad_width = 600
pad_heigth = 480
background_width = 799
background_night_SW = False

boom_time = time.time()
boom_count = 1

blue_monster_time = time.time()
blue_monster_count = 0

red_monster_time = time.time()
red_monster_count = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def check_collision_chicken_monsters():  #닭, 몬스터 충돌
    for i in blue_monsters:
        if collide(chicken, i):
            blue_monsters.remove(i)
            chicken.health -= 10
    for i in red_monsters:
        if collide(chicken, i):
            red_monsters.remove(i)
            chicken.health -= 10

def check_collision_bullet_monsters():  #총알, 몬스터 충돌
    for i in blue_monsters:
        for j in bullets:
            if collide(j, i):
                blue_monsters.remove(i)
                bullets.remove(j)
                ui.score +=10
                if chicken.skillgauge <194:
                    chicken.skillgauge +=10
    for i in red_monsters:
        for j in bullets:
            if collide(j, i):
                i.hp -=1
                if i.hp == 0:
                    red_monsters.remove(i)
                bullets.remove(j)
                ui.score +=20
                if chicken.skillgauge <194:
                    chicken.skillgauge +=10

def check_collision_missile_monsters():  #폭탄, 몬스터 충돌
    for i in blue_monsters:
        for j in missiles:
            if collide(j, i): 
                blue_monsters.remove(i)
                missiles.remove(j)
                ui.score +=10
                if chicken.skillgauge <194:
                    chicken.skillgauge +=10
    for i in red_monsters:
        for j in missiles:
            if collide(j, i):
                red_monsters.remove(i)
                missiles.remove(j)
                ui.score +=20
                if chicken.skillgauge <194:
                    chicken.skillgauge +=10
def drawObject(obj,x,y):     #그리기
    gamepad.blit(obj,(x,y))

#=========================================================폭탄그리기========================================
def blue_drawBoom():
    boom_x = blue_monster.pos_x
    boom_y = blue_monster.pos_y
    gamepad.blit(boom, (boom_x, boom_y))

def red_drawBoom():
    boom_x = red_monster.pos_x
    boom_y = red_monster.pos_y
    gamepad.blit(boom, (boom_x, boom_y))

def blue_drawBigBoom():
    boom_x = blue_monster.pos_x-25
    boom_y = blue_monster.pos_y-25
    gamepad.blit(bigboom, (boom_x, boom_y))

def red_drawBigBoom():
    boom_x = red_monster.pos_x-25
    boom_y = red_monster.pos_y-25
    gamepad.blit(bigboom, (boom_x, boom_y))
#========================================================= UI========================================



def drawScore(count): #점수표시
    font = pygame.font.SysFont(None, 40)
    text = font.render('Score:' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (pad_width*3/7, 0))


def drawBoomcount(count): #폭탄개수표시
    font = pygame.font.SysFont(None, 40)
    text = font.render('x' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (pad_width*9/10, pad_heigth*9/10))

    
def runGame():     #시작
    global gamepad, clock, chicken, background1, background2
    global blue_monsters, red_monster, bullets, ui, background_night_SW , missiles
    global blue_monster_time, blue_monster_count
    global red_monster_time, red_monster_count, missile_image

    crashed = False
    while not crashed:
        gamepad.fill(WHITE)
#==================================ras input====================================================
#==================================key board input================================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    chicken.change_pos_y = -25
                elif event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 25
                elif event.key == pygame.K_LEFT:
                    chicken.change_pos_x = -25
                elif event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 25
                elif event.key == pygame.K_LCTRL:
                    bullets.append(bullet.Bullet())
                elif event.key == pygame.K_LALT:
                    if ui.boom_count >0 :   
                        ui.boom_count-=1
                        missiles.append(bullet.Missile())
                elif event.key == pygame.K_0:
                    if chicken.skillgauge >= 194:
                        time.sleep(0.1)
                        chicken.skillgauge = 0
                        red_monsters.clear()
                        blue_monsters.clear()

                elif event.key == pygame.K_9:
                    if background_night_SW == False:
                        background_night_SW = True
                    elif background_night_SW == True:
                        background_night_SW = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    chicken.change_pos_y = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    chicken.change_pos_x = 0   #키입력
#============================몹 생성=============================================
        blue_monster_current = time.time()
        blue_monster_count = blue_monster_time - blue_monster_current 
        if (blue_monster_count < -1):
            blue_monsters.append(stage01_monster.Blue_Monster())
            blue_monster_count = -1
            blue_monster_time = time.time()

        red_monster_current = time.time()
        red_monster_count = red_monster_time - red_monster_current 
        if (red_monster_count < -2):
            red_monsters.append(stage01_monster.Red_Monster())
            red_monster_count = -2
            red_monster_time = time.time()
           





#======================================position update======================================
        chicken.pos()
        for i in blue_monsters:
            i.pos()
        for i in red_monsters:
            i.pos()
        for i in bullets:
            i.pos()
        for i in missiles:
            i.pos()
        background1.pos()
        background2.pos()

#==========================================>draw================================================

        drawObject(background1.image, background1.pos_x, 0)
        drawObject(background2.image, background2.pos_x, 0)
        if background_night_SW == 0:
            drawObject(ui.backgroundstatewindow_image, 0, 0)
            drawObject(ui.backgroundstatesun_image, 0, 0)
        elif background_night_SW == 1:
            drawObject(ui.backgroundnight_image, 0, 0)
            drawObject(ui.backgroundstatewindow_image, 0, 0)
            drawObject(ui.backgroundstatemoon_image, 0, 0)
        for i in blue_monsters:
            drawObject(i.image, i.pos_x, i.pos_y)
        for i in red_monsters:
            drawObject(i.image, i.pos_x, i.pos_y)
        drawObject(chicken.image, chicken.pos_x, chicken.pos_y)



        for i in bullets:
                drawObject(i.image,i.pos_x,i.pos_y)
        for i in missiles:
                drawObject(i.image,i.pos_x,i.pos_y)

        drawObject(ui.healthbar_image, pad_width*3/7, pad_heigth*9/10)
        drawObject(ui.skillgaugebar_imgae, pad_width * 1/18, pad_heigth * 9 / 10)
        for HP in range(chicken.health):
            drawObject(ui.health_image, HP + pad_width*3/7 + 3  , pad_heigth*9/10 + 3)
        for SG in range(chicken.skillgauge):
            drawObject(ui.skillgauge_imgae, SG + pad_width*1/18 + 3  , pad_heigth*9/10 + 3)

        drawScore(ui.score)
        drawBoomcount(ui.boom_count)
        drawObject(missile_image, pad_width * 11 / 13, pad_heigth * 9 / 10)



        check_collision_chicken_monsters()
        check_collision_bullet_monsters()
        check_collision_missile_monsters()
        pygame.display.update()
        clock.tick(15)

    pygame.quit()
    quit()

def initGame():
    global gamepad, clock, chicken, bullets, missiles
    global blue_monsters, red_monsters, ui, missile, boom, bigboom
    global background1, background2, missile_image
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_heigth))
    pygame.display.set_caption('ChickenGun')
    chicken = chicken.Chicken()
    background1 = background.Background1()
    background2 = background.Background2()
    blue_monsters = []
    red_monsters = []
    bullets = []
    missiles = []
    missile_image = pygame.image.load('resources/images/missile.png')
    ui = ui.Ui()
    clock = pygame.time.Clock()
    runGame()

initGame()
