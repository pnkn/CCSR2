import pygame

# map screen and tile size constants
tile_size = 32
map_width = 12  # 384
map_height = 9  # 288


class Toons(pygame.sprite.Sprite):

    def __init__(self, width=tile_size, height=tile_size):
        super(Toons, self).__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 0, 0))

        self.set_properties()

        self.h_speed = 0
        self.v_speed = 0

    def set_properties(self):
        self.rect = self.image.get_rect()

        self.origin_x = self.rect.centerx
        self.origin_y = self.rect.centery

    def change_speed(self, h_speed, v_speed):
        self.h_speed = h_speed
        self.v_speed = v_speed

    def set_pos(self, x, y):
        self.rect.x = x - self.origin_x
        self.rect.y = y - self.origin_y

    def set_image(self, filename=None):
        if filename is not None:
            self.image = pygame.image.load(filename)
            self.set_properties()

    def up_date(self):
        self.rect.x += self.h_speed
        self.rect.y += self.v_speed


# sprite group, sprites must be in groups to be displayed
toons_group = pygame.sprite.Group()

gus = Toons()
gus.set_image("gus.png")
gus.set_pos(384/2, 288/2)

# for testing collision detection
sand_block = Toons()
sand_block.set_image("sand.png")
sand_block.set_pos(105, 105)

# adding characters to a group
toons_group.add(gus, sand_block)
