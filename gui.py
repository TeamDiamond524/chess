import pygame

from config import SCREEN_WIDTH, SCREEN_HEIGHT
from config import BOARD_WHITE, BOARD_BLACK, BOARD_WIDTH, BOARD_SIZE
from engine.board import Board

# Constants:
SQUARE_SIZE = BOARD_WIDTH // BOARD_SIZE
BOARD_REFERENCE_POINT_X = (SCREEN_WIDTH - BOARD_WIDTH) // 2
BOARD_REFERENCE_POINT_Y = (SCREEN_HEIGHT - BOARD_WIDTH) // 2

texture_cache = {}

def game_init() -> tuple[pygame.Surface, pygame.time.Clock]:
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ChessEngine")

    clock = pygame.time.Clock()

    return (screen, clock)

def draw_board(screen: pygame.Surface, board: Board):
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            color = BOARD_WHITE if (row + col) % 2 == 0 else BOARD_BLACK

            rect = (BOARD_REFERENCE_POINT_X + col * SQUARE_SIZE, BOARD_REFERENCE_POINT_Y + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

            piece = board[row][col]

            if piece is not None:
                piece_hash = f"{piece.color}{piece.kind}"
                if texture_cache.get(piece_hash) is None:
                    texture = pygame.image.load(f"assets/pieces/{piece.color.value}-{piece.kind.value}.png").convert_alpha()
                    texture = pygame.transform.smoothscale(texture, (SQUARE_SIZE, SQUARE_SIZE))
                    texture_cache[piece_hash] = texture

                screen.blit(texture_cache[piece_hash], (rect[0], rect[1]))


def check_if_mouse_on_board(position) -> bool:
    board_dimentions = (BOARD_REFERENCE_POINT_X, BOARD_REFERENCE_POINT_Y, BOARD_REFERENCE_POINT_X + SQUARE_SIZE * BOARD_SIZE, BOARD_REFERENCE_POINT_Y + SQUARE_SIZE * BOARD_SIZE)

    #          |---------------------------Check x coordinate---------------------------|    |---------------------------Check y coordinate---------------------------|
    return not ((position[0] < board_dimentions[0] or position[0] > board_dimentions[2] ) or ( position[1] < board_dimentions[1] or position[1] > board_dimentions[3]))

def select_square(mouse_position) -> tuple[int, int] | None:
    print(check_if_mouse_on_board(mouse_position))
    if check_if_mouse_on_board(mouse_position):
        x, y = mouse_position

        col = (x - BOARD_REFERENCE_POINT_X) // SQUARE_SIZE
        row = (y - BOARD_REFERENCE_POINT_Y) // SQUARE_SIZE

        print(f"Board square [{row}][{col}]")
        print(x, y)

        return row, col
    return None

def draw_legal_moves(screen: pygame.Surface, legal_moves: list[tuple[int, int]]):
    radius = 15
    if not legal_moves:
        return
    for row, col in legal_moves:
        overlay = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        square_coordinates = (BOARD_REFERENCE_POINT_X + col * SQUARE_SIZE, BOARD_REFERENCE_POINT_Y + row * SQUARE_SIZE)
        circle_center = (SQUARE_SIZE // 2, SQUARE_SIZE // 2)
        color = (154, 219, 218, 128)

        pygame.draw.circle(overlay, color, circle_center, radius)

        screen.blit(overlay, square_coordinates)
