import pygame

from gui import game_init, draw_board, select_square, draw_legal_moves, draw_box
from engine.board import Board
from engine.move import move_to, get_legal_moves
from engine.turn_logic import change_turn, get_whose_turn
from config import BOARD_WIDTH, BOARD_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH

# Constants and other variables
SELECTED_SQUARE: None | tuple[int, int] = None 
BOARD: "Board" = Board()
CURRENT_LEGAL_MOVES = []


SQUARE_SIZE = BOARD_WIDTH // BOARD_SIZE
BOARD_REFERENCE_POINT_X = (SCREEN_WIDTH - BOARD_WIDTH) // 2
BOARD_REFERENCE_POINT_Y = (SCREEN_HEIGHT - BOARD_WIDTH) // 2

def main():
    print("Hello from chess!")

    screen, clock = game_init()

    running = True

    BOARD.set_up()

    while running:
        screen.fill("blue")

        running = event_handler(screen)

        draw_board(screen, BOARD)
        draw_legal_moves(screen, CURRENT_LEGAL_MOVES, BOARD)

        box_width = 100
        box_height = 50
        box = (BOARD_REFERENCE_POINT_X, BOARD_REFERENCE_POINT_Y * 2, BOARD_REFERENCE_POINT_X + box_width, BOARD_REFERENCE_POINT_Y * 2 + box_height)
        #draw_box(screen, box)
        pygame.display.flip()

        clock.tick(60)


def event_handler(screen) -> bool:
    global SELECTED_SQUARE
    global CURRENT_LEGAL_MOVES
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                return False
            case pygame.MOUSEBUTTONDOWN:
                # Test to get col and row of a board
                print("Selected_square = ", SELECTED_SQUARE)
                if SELECTED_SQUARE is None:
                    SELECTED_SQUARE = select_square(event.pos)
                    #print(f"Legal moves = {CURRENT_LEGAL_MOVES}")
                    print(f"Current turn: {get_whose_turn()}")
                    if SELECTED_SQUARE is not None:
                        if BOARD.get_square(SELECTED_SQUARE) is not None:
                            if get_whose_turn().value != BOARD.get_square(SELECTED_SQUARE).color.value:
                                SELECTED_SQUARE = None
                        if BOARD.get_square(SELECTED_SQUARE) is None:
                            SELECTED_SQUARE = None
                    CURRENT_LEGAL_MOVES = get_legal_moves(BOARD, SELECTED_SQUARE)
                else:
                    dest_square = select_square(event.pos)
                    if dest_square is not None:
                        if move_to(BOARD, SELECTED_SQUARE, dest_square):
                            change_turn()
                        SELECTED_SQUARE = None
                        CURRENT_LEGAL_MOVES = []

                print("Selected_square = ", SELECTED_SQUARE)
            case pygame.K_a:
                box = (BOARD_REFERENCE_POINT_X, BOARD_REFERENCE_POINT_Y * 2, BOARD_REFERENCE_POINT_X + box_width, BOARD_REFERENCE_POINT_Y * 2 + box_height)
                draw_box(screen, box)
                
    return True

if __name__ == "__main__":
    main()
