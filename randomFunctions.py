from main import *
import pygame

# creating font object for message_to_screen function
font = pygame.font.SysFont(None, 25)


def message_to_screen(text, color):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [150, 150])
    pygame.display.flip()
