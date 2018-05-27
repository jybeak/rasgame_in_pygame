import pygame
import main

pad_width = 600
pad_heigth = 480

class Bullet:
    def __init__(self):
        self.pos_x = main.chicken.pos_x + 80
        self.pos_y = main.chicken.pos_y + 25
        self.image = pygame.image.load('resources/images/bullet.png')
        self.change_pos_x = 15

    def pos(self):
        self.pos_x += self.change_pos_x
        if self.pos_x > 500:
            del(self)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 14, self.pos_y + 14




class Missile:
    def __init__(self):
        self.pos_x = main.chicken.pos_x + 80
        self.pos_y = main.chicken.pos_y + 25
        self.image = pygame.image.load('resources/images/missile.png')
        self.boomimage = pygame.image.load('resources/images/bigboom.png')
        self.change_pos_x = 10

    def pos(self):
        self.pos_x += self.change_pos_x
        if self.pos_x > 500:
            del(self)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 14, self.pos_y + 14