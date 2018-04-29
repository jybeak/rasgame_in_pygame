import pygame

pad_width = 600
pad_heigth = 480

class Chicken:
    image = pygame.image.load('resources/images/chicken.png')
    change_pos_x = 0
    change_pos_y = 0
    pos_x = pad_width * 0.05
    pos_y = pad_heigth * 0.4