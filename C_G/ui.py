import pygame
pad_width = 600
pad_heigth = 480

class Ui:
    health_image = pygame.image.load("resources/images/health.png")
    healthbar_image = pygame.image.load('resources/images/healthbar.png')
    skillgauge_imgae = pygame.image.load('resources/images/skillgauge.png')
    skillgaugebar_imgae = pygame.image.load('resources/images/skillgaugebar.png')
    backgroundstatewindow_image = pygame.image.load('resources/images/backgroundstatewindow.png')
    backgroundstatesun_image = pygame.image.load('resources/images/backgroundstatesun.png')
    backgroundstatemoon_image = pygame.image.load('resources/images/backgroundstatemoon.png')
    backgroundnight_image = pygame.image.load('resources/images/background_night.png')
    score = 0
    boom_count = 3

