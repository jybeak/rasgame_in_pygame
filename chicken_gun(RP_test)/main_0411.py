#Import library
import math
import RPi.GPIO as GPIO
import time
import random
import pygame
from pygame.locals import *

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

pygame.init()
pygame.mixer.init()
pad_width, pad_height = 640, 480
screen = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption("개발중")
FPS = 30
fpsClock=pygame.time.Clock()


keys = [False, False, False, False]
player_pos = [100, 100]
acc = [0, 0]
bullets = []
monster_timer = 100
monster_timer1 = 0
monsters_pos = [[640, 100]]
health_value = 194


player = pygame.image.load("resources/images/chicken.png")
grass = pygame.image.load("resources/images/grass.png")
redbullet = pygame.image.load("resources/images/bullet.png")
blue_monster = pygame.image.load("resources/images/blue_monster.png")


running = 1

while running:
    screen.fill(0)

    for x in range(pad_width//grass.get_width()+1):
        for y in range(pad_height//grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))



    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (player_pos[1] + 32), position[0] - (player_pos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (player_pos[0] - playerrot.get_rect().width / 2, player_pos[1] - playerrot.get_rect().height / 2)
    screen.blit(player, (player_pos[0],player_pos[1]))

    for bullet in bullets:
        index = 0
        bullet[0] += 40
        if bullet[0]<-64 or bullet[0]>640:
            bullets.pop(index)
        #화살을 그려주고 제거하는 역할
        index += 1
        screen.blit(redbullet, (bullet[0], bullet[1]))


    monster_timer -= 1
    if monster_timer == 0:
        monsters_pos.append([640, random.randint(50, 430)])
        monster_timer = 100 - (monster_timer1 * 2)
        if monster_timer1 >= 35:
            monster_timer1 = 35
        else:
            monster_timer1 += 5
    index = 0
    for badguy in monsters_pos:
        if badguy[0] < -64:
            monsters_pos.pop(index)
        badguy[0] -= 7
        # 6.3.1 - Attack castle
        badrect = pygame.Rect(blue_monster.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            monsters_pos.pop(index)

        # 충돌체크
        index1 = 0
        for bullet in bullets:
            bullrect = pygame.Rect(redbullet.get_rect())
            bullrect.left = bullet[0]
            bullrect.top = bullet[1]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                monsters_pos.pop(index)
                bullets.pop(index1)
            index1 += 1
        # 6.3.3 - Next bad guy
        index += 1
    for badguy in monsters_pos:
        screen.blit(blue_monster, badguy)

    pygame.display.flip()
    fpsClock.tick(FPS)
    if GPIO.input(17) == 1:
        acc[1] += 1
        bullets.append([playerpos1[0] + 132, playerpos1[1] + 82])
        
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True

        if event.type == KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False
        if event.type == QUIT:
            pygame.quit()
            exit(0)
        

    if keys[0]:
        player_pos[1] -= 15
    elif keys[2]:
        player_pos[1] += 15
    if keys[1]:
        player_pos[0] -= 15
    elif keys[3]:
        player_pos[0] += 15

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
