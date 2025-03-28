import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.SHOT_TIMER = 0

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw (self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.SHOT_TIMER -= dt
        if keys[pygame.K_a]:
            return self.rotate(dt * -1)
        if keys[pygame.K_d]:
            return self.rotate(dt)
        if keys[pygame.K_w]:
            return self.move(dt)
        if keys[pygame.K_s]:
            return self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            if self.SHOT_TIMER > 0:
                pass
            else:
                return self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        new_shot = Shot(self.position.x, self.position.y)
        new_shot.velocity = pygame.Vector2(0,1)
        new_shot.velocity = new_shot.velocity.rotate(self.rotation)
        new_shot.velocity = new_shot.velocity * PLAYER_SHOOT_SPEED
        self.SHOT_TIMER = PLAYER_SHOT_COOLDOWN
