import pygame
import random

pad_width = 600
pad_heigth = 480

class Blue_Monster:
    image = pygame.image.load('resources/images/blue_monster.png')
    change_pos_x = 0
    pos_x = pad_width
    pos_y = random.randrange(0, pad_heigth - 50)

    def pos(self):
        self.pos_x -= 20
        if self.pos_x <= -40:
            self.pos_x = pad_width + 30
            self.pos_y = random.randrange(0, pad_heigth - 50)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 45, self.pos_y + 49


class Red_Monster:
    image = pygame.image.load('resources/images/red_monster.png')
    change_pos_x = 0
    health = 2
    pos_x = pad_width
    pos_y = random.randrange(0, pad_heigth - 50)
    rect = pygame.Rect(image.get_rect())

    def pos(self):
        self.pos_x -= 10
        if self.pos_x <= -40:
            self.pos_x = pad_width + 30
            self.pos_y = random.randrange(0, pad_heigth - 50)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 45, self.pos_y + 49