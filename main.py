import pygame

from gui import game_init, draw_board
from engine.board import Board

def main():
    print("Hello from chess!")

    screen, clock = game_init()

    running = True

    board = Board()
    board.set_up()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("blue")

        draw_board(screen, board)

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
