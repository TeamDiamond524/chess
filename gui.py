import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from config import BOARD_WHITE, BOARD_BLACK, BOARD_WIDTH, BOARD_SIZE
from engine.board import Board

# Constants:
SQUARE_SIZE = BOARD_WIDTH // BOARD_SIZE

texture_cache = {}


def game_init() -> tuple[pygame.Surface, pygame.time.Clock]:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ChessEngine")

    clock = pygame.time.Clock()

    return (screen, clock)

def draw_board(screen: pygame.Surface, board: Board):
    reference_point_x = (SCREEN_WIDTH - BOARD_WIDTH) // 2
    reference_point_y = (SCREEN_HEIGHT - BOARD_WIDTH) // 2
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            color = BOARD_WHITE if (row + col) % 2 == 0 else BOARD_BLACK

            rect = (reference_point_x + row * SQUARE_SIZE, reference_point_y + col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

            piece = board[col][row]

            if piece is not None:
                piece_hash = f"{piece.color}{piece.kind}"
                if texture_cache.get(piece_hash) is None:
                    texture = pygame.image.load(f"assets/pieces/{piece.color.value}-{piece.kind.value}.png").convert_alpha()
                    texture = pygame.transform.smoothscale(texture, (SQUARE_SIZE, SQUARE_SIZE))
                    texture_cache[piece_hash] = texture

                screen.blit(texture_cache[piece_hash], (rect[0], rect[1]))
