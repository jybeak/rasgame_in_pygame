import pygame
import main

pad_width = 600
pad_heigth = 480


class Bullet:
    image = pygame.image.load('resources/images/bullet.png')
    pos_x = main.chicken.pos_x + 80
    pos_y = main.chicken.pos_y + 25

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 14, self.pos_y + 14