import pygame

# map screen and tile size constants
tile_size = 32
map_width = 12  # 384
map_height = 9  # 288

# texture constants
GRASS = 0
SAND = 1
CEMENT = 2

# putting an image to the constants
textures = {
    GRASS: pygame.image.load("grass.png"),
    SAND: pygame.image.load("sand.png"),
    CEMENT: pygame.image.load("cement.png")
}

# a few map screens for testing
tile_set_1 = [
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]

tile_set_2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class Map(object):

    def __init__(self, tile_set):
        self.tile_set = tile_set

    def draw_map(self, game_screen):
        # drawing the tiles to the game screen
        for row in range(map_height):
            for column in range(map_width):
                game_screen.blit(textures[self.tile_set[row][column]], (column*tile_size, row*tile_size))

'''
    def screen_trans(self):
        # move current rect to player direction, while bringing in the next rect at the same time
        # place toon in new screen at a certain point? wait a few milliseconds?

    def get_current_screen(self):
        current_screen = ""
        current_rect = ""


    def get_next_screen(self):
        next_screen = ""
        next rect = ""

    def move_rects(self):
        current_rect.move()?
        next_rect.move()?

'''

# creating a few screens of the entire map for testing
this_map = Map(tile_set_1)
next_map = Map(tile_set_2)
