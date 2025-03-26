import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_clock = pygame.time.Clock()
    dt = 0
    Updatable_group = pygame.sprite.Group()
    Drawable_group = pygame.sprite.Group()
    Player.containers = (Updatable_group, Drawable_group)
    User_Player = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    Asteroid_group = pygame.sprite.Group()
    Asteroid.containers = (Updatable_group, Drawable_group, Asteroid_group)
    Field_group = pygame.sprite.Group()
    AsteroidField.containers = (Updatable_group)
    New_Field = AsteroidField()
    Shot_group = pygame.sprite.Group()
    Shot.containers = (Updatable_group, Drawable_group, Shot_group)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000000)
        Updatable_group.update(dt)
        for asteroid in Asteroid_group:
            if asteroid.collision(User_Player):
                raise Exception("Game over!")
        for asteroid in Asteroid_group:
            for shot in Shot_group:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.kill()
        for item in Drawable_group:
            item.draw(screen)
        pygame.display.flip()
        dt = screen_clock.tick(60)/1000


if __name__ == "__main__":
    main()