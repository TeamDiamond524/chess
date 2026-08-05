import pygame

from gui import game_init


def main():
    print("Hello from chess!")
    
    screen, clock = game_init()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("blue")


        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
