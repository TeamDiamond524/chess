import pygame

from gui import game_init, draw_board, event_handler
from engine.board import Board

def main():
    print("Hello from chess!")

    screen, clock = game_init()

    running = True

    board = Board()
    board.set_up()

    while running:
        running = event_handler()

        screen.fill("blue")

        draw_board(screen, board)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
