import pygame

pad_width = 600
pad_heigth = 480

class Chicken:
    image = pygame.image.load('resources/images/chicken.png')
    health = 194
    change_pos_x = 0
    change_pos_y = 0
    pos_x = pad_width * 0.05
    pos_y = pad_heigth * 0.4

    def pos(self):
        self.pos_x += self.change_pos_x
        self.pos_y += self.change_pos_y
        if self.pos_x < -30:
            self.pos_x = -30
        elif self.pos_x > pad_width - 30:
            self.pos_x = pad_width - 30
        if self.pos_y < -30:
            self.pos_y = -30
        elif self.pos_y > pad_heigth - 30:
            self.pos_y = pad_heigth - 30