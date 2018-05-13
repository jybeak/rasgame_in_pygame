import pygame

pad_width = 600
pad_heigth = 480


class Bullet:
    image = pygame.image.load('resources/images/bullet.png')
    change_pos_x = 15
    pos_x = -200
    def pos(self):
        self.pos_x += self.change_pos_x
        if self.pos_x > 400:
            del(self)

    def get_bb(self):
        return self.pos_x, self.pos_y, self.pos_x + 14, self.pos_y + 14