from randomFunctions import *
from pygame.locals import *
from Toons import *
from Maps import *
import pygame

clock = pygame.time.Clock()
FPS = 60

# color constants
GREEN = (0, 210, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# map screen and tile size constants
tile_size = 32
map_width = 12  # 384
map_height = 9  # 288

# initializing pygame and making a surface
pygame.init()
game_screen = pygame.display.set_mode((map_width*tile_size, map_height*tile_size))
pygame.display.set_caption("Cartoon Cartoon Summer Resort 2")


# i need to study surfaces, sprites, rects, convert, all that stuff

# draw the map screens a different way also? see if someones tile generator can help things
# basically, i need to be able to turn the screen into a rect so i can move it out, and move the new one in
# then place the toon in its new spot on the new screen
# unless there's some way to screen transition that's better/simpler

# main function
def main():

    # main loop for program
    while True:

        # handling the exit button
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and \
                            event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gus.change_speed(-10, 0)
                if event.key == pygame.K_RIGHT:
                    gus.change_speed(10, 0)
                if event.key == pygame.K_UP:
                    gus.change_speed(0, -10)
                if event.key == pygame.K_DOWN:
                    gus.change_speed(0, 10)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    gus.change_speed(10, 0)
                if event.key == pygame.K_RIGHT:
                    gus.change_speed(-10, 0)
                if event.key == pygame.K_UP:
                    gus.change_speed(0, 10)
                if event.key == pygame.K_DOWN:
                    gus.change_speed(0, -10)

        clock.tick(FPS)

        this_map.draw_map(game_screen)

        gus.up_date(collidable_objects)

        if pygame.sprite.collide_rect(gus, sand_block):
            message_to_screen("collision!", BLACK)

        toons_group.draw(game_screen)

        pygame.display.update()

if __name__ == '__main__':
    main()
