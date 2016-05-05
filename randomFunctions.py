from main import *
import pygame


def useless_function():
    print("ello guvnuh")


font = pygame.font.SysFont(None, 25)


def message_to_screen(text, color):
    screen_text = font.render(text, True, color)
    game_screen.blit(screen_text, [150, 150])
    pygame.display.flip()
