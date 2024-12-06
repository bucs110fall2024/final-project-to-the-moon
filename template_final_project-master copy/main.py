import pygame
from src.Controller import Controller

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slides and Ladders")

    controller = Controller(screen)
    controller.run()

if __name__ == '__main__':
    main()
