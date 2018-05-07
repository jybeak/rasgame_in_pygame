import pygame
import random

pad_width = 600
pad_heigth = 480

class Blue_Monster:
    image = pygame.image.load('resources/images/blue_monster.png')
    change_pos_x = 0
    pos_x = pad_width
    pos_y = random.randrange(0, pad_heigth)

    def pos(self):
        self.pos_x -= 20
        if self.pos_x <= -40:
            self.pos_x = pad_width + 30
            self.pos_y = random.randrange(0, pad_heigth)


class Red_Monster:
    image = pygame.image.load('resources/images/red_monster.png')
    change_pos_x = 0
    pos_x = pad_width
    pos_y = random.randrange(0, pad_heigth)


    def pos(self):
        self.pos_x -= 10
        if self.pos_x <= -40:
            self.pos_x = pad_width + 30
            self.pos_y = random.randrange(0, pad_heigth)