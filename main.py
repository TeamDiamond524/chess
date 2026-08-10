import pygame

from gui import game_init, draw_board, select_square, draw_legal_moves
from engine.board import Board
from engine.move import move_to, get_legal_moves

# Constants and other variables
SELECTED_SQUARE: None | tuple[int, int] = None 
BOARD: "Board" = Board()
CURRENT_LEGAL_MOVES = []

def main():
    print("Hello from chess!")

    screen, clock = game_init()

    running = True

    BOARD.set_up()

    while running:
        running = event_handler()

        screen.fill("blue")

        draw_board(screen, BOARD)
        draw_legal_moves(screen, CURRENT_LEGAL_MOVES)

        pygame.display.flip()

        clock.tick(60)


def event_handler() -> bool:
    global SELECTED_SQUARE
    global CURRENT_LEGAL_MOVES
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                return False
            case pygame.MOUSEBUTTONDOWN:
                # Test to get col and row of a board
                if SELECTED_SQUARE is None:
                    SELECTED_SQUARE = select_square(event.pos)
                    CURRENT_LEGAL_MOVES = get_legal_moves(BOARD, SELECTED_SQUARE)
                    print(f"Legal moves = {CURRENT_LEGAL_MOVES}")
                else:
                    dest_square = select_square(event.pos)
                    if dest_square is not None:
                        move_to(BOARD, SELECTED_SQUARE, dest_square)
                        SELECTED_SQUARE = None
                        CURRENT_LEGAL_MOVES = []
    return True

if __name__ == "__main__":
    main()
