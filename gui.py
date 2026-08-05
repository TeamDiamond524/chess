import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT

def game_init() -> tuple[pygame.Surface, pygame.time.Clock]:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ChessEngine")

    clock = pygame.time.Clock()

    return (screen, clock)
