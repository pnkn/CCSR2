import pygame, sys
from pygame.locals import *

clock = pygame.time.Clock()
FPS = 60

# color constants
GREEN = (0, 210, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# map screen and tile size constants
tile_size = 32
map_width = 12  # 384
map_height = 9  # 288

# a single map screen
tile_set_1 = [
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT, CEMENT],
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, CEMENT, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, SAND, CEMENT, SAND, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, SAND, SAND, SAND, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS]
]


class Map(object):

    def __init__(self, tile_set=""):
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

# i think the next step would be to expand the toon class?
# should i be drawing the sprites a different way? i need to study surfaces, sprites, rects, convert, all that stuff

# draw the map screens a different way also? see if someones tile generator can help things
# basically, i need to be able to turn the screen into a rect so i can move it out, and move the new one in
# then place the toon in its new spot on the new screen
# unless there's some way to screen transition that's better/simpler


class Toons(pygame.sprite.Sprite):

    def __init__(self, name="", sprite_1=""):
        self.name = name
        self.sprite_1 = sprite_1
        self.x = 0
        self.y = 0
        self.current_pos = ""
        self.rect = ""

    def draw_self(self, game_screen):
        game_screen.blit(self.sprite_1, (self.x, self.y))

    def move_self(self):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[K_UP]:
            self.y -= 9
        if keys[K_DOWN]:
            self.y += 9
        if keys[K_LEFT]:
            self.x -= 9
        if keys[K_RIGHT]:
            self.x += 9

    def check_edge(self):
        if self.x >= 384 - tile_size:
            print("right")
        elif self.x < 0:
            print("left")                        # i want this function to work with the screen transition function
        elif self.y >= 288 - tile_size:          # it only prints out the direction right now for place holding
            print("down")
        elif self.y < 0:
            print("up")

    '''
    def get_current_pos(self):
        self.current_pos = (self.x, self.y)          this function doesn't work like i want it to
        return self.current_pos

    def set_new_pos(self):
                                                     will set toon in new spot for new screen?

    '''

# creating the first instance of the Toons class, gus
gus = Toons(name="gus", sprite_1=pygame.image.load("gus.png"))

# creating one screen of the entire map
this_map = Map(tile_set_1)


# main program loop
def main():
    # initializing pygame and making a surface
    pygame.init()
    game_screen = pygame.display.set_mode((map_width*tile_size, map_height*tile_size))
    pygame.display.set_caption("Cartoon Cartoon Summer Resort 2")
    # screen_rect = game_screen.get_rect()

    # fill background (not sure if this is needed)
    background = pygame.Surface(game_screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # display text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello there", 1, (10, 10, 10))
    text_pos = text.get_rect()
    text_pos.centerx = background.get_rect().centerx
    background.blit(text, text_pos)

    # main loop for program
    while True:

        # handling the exit button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()

        gus.move_self()

        gus.check_edge()  # this function will be involved with screen transitions, eventually

        this_map.draw_map(game_screen)

        gus.draw_self(game_screen)

        pygame.display.update()

        clock.tick(FPS)

if __name__ == '__main__':
    main()
