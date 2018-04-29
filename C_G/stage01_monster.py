import pygame
import random

pad_width = 600
pad_heigth = 480

class Blue_Monster:
    image = pygame.image.load('resources/images/blue_monster.png')
    change_pos_x = 0
    pos_x = pad_width
    pos_y = random.randrange(0, pad_heigth)