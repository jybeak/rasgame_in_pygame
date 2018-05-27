import pygame
import random

pad_width = 600
pad_heigth = 480

class Blue_Monster:
    def __init__(self):
        self.pos_x = pad_width
        self.pos_y = random.randrange(0, pad_heigth - 50)
        self.change_pos_y = random.randint(-8, 8)
        self.image = pygame.image.load('resources/images/blue_monster.png')
        self.deathimage = pygame.image.load('resources/images/boom.png')

    def pos(self):
        self.pos_x -= 20
        self.pos_y += self.change_pos_y
        if self.pos_x <= -40:
            del(self)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 45, self.pos_y + 49


class Red_Monster:
    def __init__(self):
        self.pos_x = pad_width
        self.pos_y = random.randrange(0, pad_heigth - 50)
        self.change_pos_y = random.randint(-5, 5)
        self.image = pygame.image.load('resources/images/red_monster.png')
        self.deathimage = pygame.image.load('resources/images/boom.png')
        self.hp = 2

    def pos(self):
        self.pos_x -= 10
        self.pos_y += self.change_pos_y
        if self.pos_x <= -40:
            del(self)
    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 45, self.pos_y + 49