from main import *
import pygame


# color constants
GREEN = (0, 210, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Buildings(pygame.sprite.Sprite):

    def __init__(self, width=0, height=0):
        super(Buildings, self).__init__()

        self.image = pygame.Surface((width, height))

        self.set_properties()

    def set_properties(self):
        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    def set_pos(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pygame.image.load(filename)
            self.set_properties()


class Doors(pygame.sprite.Sprite):
    def __init__(self, color=WHITE, width=32, height=32):
        super(Doors, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.set_properties()

    def set_properties(self):
        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pygame.image.load(filename)
            self.set_properties()


buildings_group = pygame.sprite.Group()

disco = Buildings()
disco.set_image("disco.png")
disco.set_pos(280, 25)

buildings_group.add(disco)

# --------------------

doors_group = pygame.sprite.Group()

door = Doors()
door.set_image("cement.png")
door.set_pos(264, 75)

doors_group.add(door)



