import pygame
import random

def main():
    WIDTH = 360
    HEIGHT = 480
    FPS = 30

    # Colors (R, G, B)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # initialize LIB
    pygame.init()
    pygame.mixer.init()

    # main window of program
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption ("Test game")

    # check FPS
    clock = pygame.time.Clock()

    running = True
    while running:
        # Stop cycle on right speed
        clock.tick()

        # Waits for events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        #Updates
        print(__name__)

        # Rendering
        screen.fill(BLACK)
        # Flip outdrawed screen, with drawed element
        pygame.display.flip()
if __name__ == '__main__':
    main()