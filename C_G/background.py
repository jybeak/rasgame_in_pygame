import pygame

background_width = 799

class Background1:
    image = pygame.image.load('resources/images/background.png')
    pos_x = 0
    def pos(self):
        self.pos_x -= 2
        if self.pos_x < -background_width:
            self.pos_x = 0

class Background2:
    image = pygame.image.load('resources/images/background.png')
    pos_x = background_width

    def pos(self):
        self.pos_x -= 2
        if self.pos_x < 0:
            self.pos_x = background_width