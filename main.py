import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_clock = pygame.time.Clock()
    dt = 0
    User_Player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        User_Player.draw(screen)
        User_Player.update(dt)
        pygame.display.flip()
        dt = screen_clock.tick(60)/1000


if __name__ == "__main__":
    main()